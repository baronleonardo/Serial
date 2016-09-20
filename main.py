import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from MainWindow import Ui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    # window.centralWidget
    sys.exit(app.exec_())
