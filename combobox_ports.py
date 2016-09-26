from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt
from Serial import Serial
from PyQt5.QtWidgets import QMessageBox


class ComboBox_Ports(QComboBox):
	"""docstring for ComboBox_Ports"""

	lst = []
	last = -1

	def __init__(self, parent=None):
		super(ComboBox_Ports, self).__init__(parent)
		self.parent = parent
		self.activated.connect(self.onCurrentIndexChanged)

	def updateList(self):

		self.lst = Serial.get_available_ports_systemLocations_and_manufacturers()

		manufacture = 1
		locations = 0

		for index in range(0, len(self.lst)):
			self.addItem(self.lst[index][manufacture])
			self.setItemData(index, self.lst[index][locations], Qt.ToolTipRole)

	def showPopup(self):
		self.clear()
		self.updateList()

		if self.lst == []:
			QMessageBox.warning(self.parent, "Warning", "No device attached", QMessageBox.Ok, QMessageBox.NoButton)

		super(ComboBox_Ports, self).showPopup()

	def onCurrentIndexChanged(self, index):

		if self.last != index:
			self.last = index