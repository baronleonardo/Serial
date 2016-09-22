from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

class Serial(QSerialPort):
    def __init__(self, parent=None):
        super(Serial, self).__init__(parent)
        self.parent      = parent
        self.baudRate    = self.Baud9600
        self.dataBits    = self.Data8
        self.parity      = self.NoParity
        self.stopBits    = self.OneStop
        self.flowControl = self.NoFlowControl

    def get_available_ports_systemLocations_and_manufacturers(self):
        available_ports = QSerialPortInfo.availablePorts()
        ports_info = []

        for port in available_ports:
            ports_info.append( (port.systemLocation(), port.manufacturer()) )

        return ports_info