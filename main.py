import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login_window import Ui_LoginWindow
from send_window import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

    def open_second_window(self):
        self.second_window = QMainWindow()
        self.second_ui = Ui_MainWindow()
        self.second_ui.setupUi(self.second_window)
        self.second_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()

    window.ui.loginPushButton.clicked.connect(window.open_second_window)
    app.exec()
