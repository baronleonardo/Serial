from PyQt5.QtChart import QChartView, QChart, QLineSeries
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtCore import Qt, QEvent

class ChartView(QChartView):
    """docstring for ChartView"""

    x = 0
    is_chart_drawing = True
    max_y = 0
    min_y = 0
    counter_X = 0
    counter_Y = 0

    def __init__(self, parent=None):
        super(ChartView, self).__init__(parent)
        self.parent = parent
        self.chart = Chart()
        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)

    def draw_point(self, y):
        if self.is_chart_drawing is True:
            self.chart.add_point(self.x, y)
            self.x += 1

            # scroll and remove old points to keep always seen points = MAX_X
            if self.x >= self.chart.MAX_X:
                self.chart.scroll(self.chart.plotArea().width() / self.chart.MAX_X, 0)
                self.chart.remove_point(0)

            self.__calculate_peak(y)

    def __calculate_peak(self, y):
        if self.counter_X == self.chart.MAX_X:
            self.max_y     = 0
            self.min_y     = 0
            self.counter_X = 0

        elif self.counter_Y == self.chart.MAX_X:
            self.max_y     = 0
            self.min_y     = 0
            self.counter_Y = 0

        if self.max_y < y:
            self.max_y = y
            self.chart.axisY().setMax(y + (0.1 * y))
            self.counter_X = 0

        elif self.min_y > y:
            self.min_y = y
            self.chart.axisY().setMin(y + (0.1 * y))
            self.counter_Y = 0

        self.counter_X += 1
        self.counter_Y += 1

    def on_pause_chart(self, state:bool):
        if state is True:
            self.is_chart_drawing = False

        else:
            self.is_chart_drawing = True

    def reset(self):
        del(self.chart)
        self.chart = Chart()
        self.setChart(self.chart)

        self.x         = 0
        self.max_y     = 0
        self.min_y     = 0
        self.counter_X = 0
        self.counter_Y = 0

class Chart(QChart):
    MIN_X = 0
    MAX_X = 750
    MIN_Y = -1
    MAX_Y = 1
    TICKS = 5
    PENCOLOR = Qt.red
    PENWIDTH = 1

    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)
        self.parent = parent
        # we will draw lines
        self.series = QLineSeries(parent)
        # color and pen-width
        self.series.setPen(QPen(self.PENCOLOR, self.PENWIDTH))

        self.addSeries(self.series)

        self.legend().hide()
        self.__construct_axises()

    def setRange_X_axis(self, min_X, max_X):
        self.MIN_X = min_X
        self.MAX_X = max_X
        self.axisX().setRange(self.MIN_X, self.MAX_X)

    def setRange_Y_axis(self, min_Y, max_Y):
        self.MIN_Y = min_Y
        self.MAX_Y = max_Y
        self.axisY().setRange(self.MIN_Y, self.MAX_Y)

    def add_point(self, x ,y):
        self.series.append(x, y)

    def get_series(self) -> list:
        return self.series.pointsVector()

    def remove_point(self, index):
        self.series.remove(index)

    def remove_points(self, index, count):
        self.series.removePoints(index, count)

    def replace_point(self, index, x, y):
        self.series.replace(index , x , y)

    def replace_series(self, lst):
        self.series.replace(lst)

    def get_series_count(self):
        return self.series.count()

    def __construct_axises(self):
        self.createDefaultAxes()

        # X-Axis
        x_axis = self.axisX()
        x_axis.hide()
        x_axis.setRange(self.MIN_X, self.MAX_X)

        # Y-axis
        y_axis = self.axisY()
        y_axis.setRange(self.MIN_Y, self.MAX_Y)
        y_axis.setTickCount(self.TICKS)