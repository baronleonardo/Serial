from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt

class ComboBox_Ports(QComboBox):
	"""docstring for ComboBox_Ports"""

	def __init__(self, parent=None):
		super(ComboBox_Ports, self).__init__(parent)
		self.parent = parent


	def updateList(self):

		# TODO: call function to get the "port info" list
		lst = []

		for index in range(0, len(lst)):
			self.addItem(lst[index][1])
			self.setItemData(index, lst[index][0], Qt.ToolTipRole)
			print(self.currentIndex())

		return


	def showPopup(self):
		self.clear()
		self.updateList()



		super(ComboBox_Ports, self).showPopup()
