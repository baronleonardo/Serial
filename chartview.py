from PyQt5.QtChart import QChartView

class ChartView(QChartView):
	"""docstring for ChartView"""
	def __init__(self, parent=None):
		super(ChartView, self).__init__(parent)
		self.parent = parent
		