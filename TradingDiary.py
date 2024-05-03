import sys
from app import App
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    
    sys.exit(app.exec())