from PyQt5.QtWidgets import QTextEdit
# from PyQt5.QtCore import pyqtSlot

class SerialOut_TextEdit(QTextEdit):
	"""docstring for SerialOut_TextEdit"""
	def __init__(self, parent):
		super(SerialOut_TextEdit, self).__init__(parent)
		self.parent = parent

	def on_input_sent(self, text):
		self.append(text)