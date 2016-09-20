from PyQt5 import uic
from PyQt5.QtChart import QChartView
from PyQt5.QtWidgets import QMainWindow

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Serial_Communications.ui', self)
        self.__signals()
        self.show()
    
    def __signals(self):
        self.page_forward_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.page_backward_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))