from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

class Serial(QSerialPort):
    def __init__(self, parent=None):
        super(Serial, self).__init__(parent)
        self.parent = parent
        self.setBaudRate = self.Baud9600
        self.setDataBits = self.Data8
        self.setParity = self.NoParity
        self.setStopBits = self.OneStop
        self.setFlowControl = self.HardwareControl


class SerialInfo(QSerialPortInfo):
    def __init__(self, parent=None):
        super(SerialInfo, self).__init__(parent)

    def get_available_ports_systemLocations_and_manufacturers(self):
        available_ports = self.availablePorts()
        ports_info = []

        for port in available_ports:
            ports_info.append( (port.systemLocation(), port.manufacturer()) )

        return ports_info