import sys
from PyQt5.QtWidgets import *
from login_window import LoginWindow
from main_window import MainWindow 


class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)

        # Initializes the login window
        self.login_window = LoginWindow()

        # Connects login success signal to the main window opening
        self.login_window.login_success.connect(self.show_main_window)


        # Shows the login window
        self.login_window.show()

    def show_main_window(self):
        # Opens the main window after successful login
        headmaster = self.login_window.comboBox_headmaster.currentText()
        self.main_window = MainWindow(headmaster)
        self.main_window.show()
        
        # Closes the login window
        self.login_window.close()

    def run(self):
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()   