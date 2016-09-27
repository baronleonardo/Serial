from PyQt5.QtChart import QChartView, QChart, QLineSeries
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtCore import Qt

class ChartView(QChartView):
    """docstring for ChartView"""
    def __init__(self, parent=None):
        super(ChartView, self).__init__(parent)
        self.parent = parent
        self.chart = Chart()
        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)

    def draw_point(self, x, y):
        self.chart.add_point(x , y)
        
class Chart(QChart):
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)
        self.parent = parent
        # we will draw lines
        self.series = QLineSeries(parent)
        # color and pen-width
        self.series.setPen(QPen(Qt.red, 1))
        self.addSeries(self.series)

        self.legend().hide()
        self.__construct_axises()

    def add_point(self, x ,y):
        self.series.append(x, y)

    def __construct_axises(self):
        self.createDefaultAxes()

        # X-Axis
        x_axis = self.axisX()
        x_axis.hide()

        # Y-axis
        y_axis = self.axisY()