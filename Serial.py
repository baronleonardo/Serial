from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

class Serial(QSerialPort):
    def __init__(self, parent=None):
        super(Serial, self).__init__(parent)
        self.parent      = parent
        self.baudRate    = self.Baud9600
        self.dataBits    = self.Data8
        self.parity      = self.NoParity
        self.stopBits    = self.OneStop
        self.flowControl = self.NoFlowControl

        # signal: ready to read, slot: begin reading
        self.readyRead.connect(self.read_data)

    def read_data(self):
        line = self.readLine().trimmed()

        if line != "":
            return line

    @staticmethod
    def get_available_ports_systemLocations_and_manufacturers():
        available_ports = QSerialPortInfo.availablePorts()
        ports_info = []

        for port in available_ports:
            ports_info.append( (port.systemLocation(), port.manufacturer()) )

        return ports_info

    def open( self, port_loc="/dev/ttyACM0", baud_rate=9600):
        self.baudRate = baud_rate
        self.setPortName(port_loc)

        if super(Serial, self).open(QIODevice.ReadWrite) == True:
            return True

        else:
            print("Can't open port %s" % port_loc)
            return False