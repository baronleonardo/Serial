from PyQt5 import uic
from PyQt5.QtChart import QChartView
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QDir

class Ui(QMainWindow):
    def __init__(self, executable_path):
        super(Ui, self).__init__()
        ui_file = executable_path + QDir.separator() + 'Serial.ui'
        uic.loadUi(ui_file, self)
        self.__signals()
        self.show()
    
    def __signals(self):
        self.page_forward_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.page_backward_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
