from PyQt5.QtWidgets import QTextEdit
# from PyQt5.QtCore import pyqtSlot

class SerialOut_TextEdit(QTextEdit):
	"""docstring for SerialOut_TextEdit"""
	def __init__(self, parent=None):
		super(SerialOut_TextEdit, self).__init__(parent)
		self.parent = parent

	def on_serial_read(self, text):
		self.append(text)

	def on_autoscroll_state_changed(self, state):
		pass