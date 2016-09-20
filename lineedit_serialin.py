from PyQt5.QtWidgets import QLineEdit

class LineEdit_SerialIn(QLineEdit):
	"""docstring for LineEdit_SerialIn"""
	def __init__(self, parent):
		super(LineEdit_SerialIn, self).__init__(parent)
		self.parent = parent
		