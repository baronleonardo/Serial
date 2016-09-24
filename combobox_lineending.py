from PyQt5.QtWidgets import QComboBox

class ComboBox_LineEnding(QComboBox):
	"""docstring for QComboBox"""
	def __init__(self, parent=None):
		super(ComboBox_LineEnding, self).__init__(parent)
		self.parent = parent
		