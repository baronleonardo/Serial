from PyQt5.QtSerialPort import QSerialPort

class Serial(QSerialPort):
    def __init__(self, parent):
        super(Serial, self).__init__(parent)
        self.parent = parent
        self.setBaudRate = self.Baud9600
        self.setDataBits = self.Data8
        self.setParity = self.NoParity
        self.setStopBits = self.OneStop
        self.setFlowControl = self.HardwareControl