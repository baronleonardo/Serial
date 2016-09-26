from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt
from Serial import Serial

class ComboBox_Ports(QComboBox):
	"""docstring for ComboBox_Ports"""

	def __init__(self, parent=None):
		super(ComboBox_Ports, self).__init__(parent)
		self.parent = parent

	def updateList(self):

		lst = Serial.get_available_ports_systemLocations_and_manufacturers()

		for index in range(0, len(lst)):
			self.addItem(lst[index][1])
			self.setItemData(index, lst[index][0], Qt.ToolTipRole)

	def showPopup(self):
		self.clear()
		self.updateList()

		super(ComboBox_Ports, self).showPopup()
