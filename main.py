import sys, os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from MainWindow import Ui

if __name__ == '__main__':
    executable_path = os.path.dirname(os.path.abspath(__file__))

    app = QApplication(sys.argv)
    window = Ui(executable_path)

    library_paths = QCoreApplication.libraryPaths()
    QCoreApplication.setLibraryPaths([executable_path] + library_paths)
    app.setStyle( "gtk2" )

    sys.exit(app.exec_())
