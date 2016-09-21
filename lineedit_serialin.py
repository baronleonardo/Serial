from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal

class LineEdit_SerialIn(QLineEdit):
	"""docstring for LineEdit_SerialIn"""

	__line_ending = "\n"

	# create a signal
	input_sent = pyqtSignal(['QString'])

	def __init__(self, parent):
		super(LineEdit_SerialIn, self).__init__(parent)
		self.parent = parent
		
	def on_return_pressed(self):
		text = self.text() + self.__line_ending
		self.input_sent.emit(text)
		self.clear()

	def on_line_ending_changed(self, line_ending_index):
		if line_ending_index == 0:
			self.__line_ending = ""

		elif line_ending_index == 1:
			self.__line_ending = "\n"

		elif line_ending_index == 2:
			self.__line_ending = "\r"

		elif line_ending_index == 3:
			self.__line_ending = "\r\n"
