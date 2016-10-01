from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt
from Serial import Serial
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtSerialPort import QSerialPort


class ComboBox_Ports(QComboBox):
    """docstring for ComboBox_Ports"""

    currentItemChanged = pyqtSignal(str)

    lst = []
    last = -1
    MANUFACTURER = 1
    LOCATION = 0

    def __init__(self, parent=None):
        super(ComboBox_Ports, self).__init__(parent)
        self.parent = parent
        self.activated.connect(self.onCurrentIndexChanged)

    def updateList(self):
        self.lst = Serial.get_available_ports_systemLocations_and_manufacturers()

        for index in range(0, len(self.lst)):
            self.addItem(self.lst[index][self.MANUFACTURER])
            self.setItemData(index, self.lst[index][self.LOCATION], Qt.ToolTipRole)

    def showPopup(self):
        self.clear()
        self.updateList()

        if self.lst == []:
            QMessageBox.warning(self.parent, "Warning", "No device attached", QMessageBox.Ok, QMessageBox.NoButton)

        super(ComboBox_Ports, self).showPopup()

    def reset(self):
        self.clear()
        self.last = -1

    def onCurrentIndexChanged(self, index):

        if self.last != index:
            loc = self.lst[index][self.LOCATION]
            self.currentItemChanged.emit(loc)
            self.last = index