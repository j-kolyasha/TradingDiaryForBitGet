import hmac
import base64
import time
import json

from enums import *
import requests

class Client:
    def __init__(self, apiKey : str, apiSecretKey : str, apiPassphrase : str):
        self._apiKey = apiKey
        self._apiSecretKey = apiSecretKey
        self._apiPassphrase = apiPassphrase
        
    def request(self, requestType : str, requestPath : str, params : str):
        if requestType == GET:
            requestPath = requestPath + self.__parse_params_to_str(params)
        
        url = API_URL + requestPath
        timestamp = self.__get_timestamp()
    
        body = json.dumps(params) if requestType == POST else ""
        sign = self.__sign(self.__pre_hash(timestamp, requestType, requestPath, str(body)), self._apiSecretKey)
        header = self.__get_header(self._apiKey, sign, timestamp, self._apiPassphrase)
        
        response = None
        if requestType == GET:
            response = requests.get(url, headers=header)
        elif requestType == POST:
            response = requests.post(url, data=body, headers=header)
        elif requestType == DELETE:
            response = requests.delete(url, headers=header)
            
        return response
    
    def getParams(self, symbol = '', productType = '', idLessThan = '', startTime = '', endTime = '', limit = ''):
        return {SYMBOL : symbol,  
                PRODUCT_TYPE: productType, 
                ID_LESS_THAN : idLessThan,
                START_TIME : startTime,
                END_TIME : endTime,
                LIMIT : limit}
    
    # "__" - meen private method    
    def __get_header(self, api_key : str, a_sign : str, timestamp : str, passphrase : str):
        header = dict()
        header[CONTENT_TYPE] = APPLICATION_JSON
        header[ACCESS_KEY] = api_key
        header[ACCESS_SIGN] = a_sign
        header[ACCESS_TIMESTAMP] = str(timestamp)
        header[ACCESS_PASSPHRASE] = passphrase

        return header
        
    def __get_timestamp(self):
        return int(time.time() * 1000)

    def __sign(self, message, secret_key):
        mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
        d = mac.digest()
        return base64.b64encode(d)

    def __pre_hash(self, timestamp, method, request_path, body ):
        return str(timestamp) + str.upper(method) + request_path + body

    def __parse_params_to_str(self, params):
        params = [(key, val) for key, val in params.items()]
        params.sort(key=lambda x: x[0])
        url = '?' + self.__toQueryWithNoEncode(params);
        if url == '?':
            return ''
        return url

    def __toQueryWithNoEncode(self, params):
        url = ''
        for key, value in params:
            url = url + str(key) + '=' + str(value) + '&'
        return url[0:-1]
    