import sys, os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from MainWindow import Ui

if __name__ == '__main__':
    executable_path = os.path.dirname(os.path.abspath(__file__))

    app = QApplication(sys.argv)
    window = Ui(executable_path)
    sys.exit(app.exec_())
