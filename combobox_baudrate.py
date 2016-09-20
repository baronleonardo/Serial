from PyQt5.QtWidgets import QComboBox

class ComboBox_BaudRate(QComboBox):
	"""docstring for ComboBox_BaudRate"""
	def __init__(self, parent):
		super(ComboBox_BaudRate, self).__init__(parent)
		self.parent = parent
		