from PyQt5.QtWidgets import QComboBox

class ComboBox_Ports(QComboBox):
	"""docstring for LineEdit_SerialIn"""

	def __init__(self, parent=None):
		super(ComboBox_Ports, self).__init__(parent)
		self.parent = parent
