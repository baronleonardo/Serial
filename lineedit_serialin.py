from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal

class LineEdit_SerialIn(QLineEdit):
	"""docstring for LineEdit_SerialIn"""

	# create a signal
	input_sent = pyqtSignal(['QString'])

	def __init__(self, parent):
		super(LineEdit_SerialIn, self).__init__(parent)
		self.parent = parent
		
	def on_return_pressed(self):
		self.input_sent.emit(self.text())
		self.clear()