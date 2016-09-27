from PyQt5.QtChart import QChartView, QChart, QLineSeries

class ChartView(QChartView):
    """docstring for ChartView"""
    def __init__(self, parent=None):
        super(ChartView, self).__init__(parent)
        self.parent = parent
        
class Chart(QChart):
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)
        self.parent = parent
        self.series = QLineSeries(parent)

    def add_point(self, x ,y):
        self.series.append(x, y)