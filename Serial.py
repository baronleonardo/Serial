from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice, pyqtSignal

class Serial(QSerialPort):

    # Signal
    readyRead = pyqtSignal(['QByteArray'])

    def __init__(self, port_loc="/dev/ttyACM0", baud_rate=9600, parent=None):
        super(Serial, self).__init__(parent)
        self.parent      = parent
        self.baudRate    = baud_rate
        self.dataBits    = self.Data8
        self.parity      = self.NoParity
        self.stopBits    = self.OneStop
        self.flowControl = self.NoFlowControl
        self.setPortName(port_loc)

        # signal: ready to read, slot: format data
        super(Serial, self).readyRead.connect(self.format_data)

    def format_data(self):
        line = self.readLine().trimmed()

        if line != "":
            self.readyRead['QByteArray'].emit(line)

    def write(self, data:bytes):
        super(Serial, self).write(data)
        self.flush()

    def write_line(self, data:str):
        for character in data:
            self.write(character.encode("ascii"))

    @staticmethod
    def get_available_ports_systemLocations_and_manufacturers():
        available_ports = QSerialPortInfo.availablePorts()
        ports_info = []

        for port in available_ports:
            ports_info.append( (port.systemLocation(), port.manufacturer()) )

        return ports_info

    def open(self):
        if super(Serial, self).open(QIODevice.ReadWrite) is True:
            return True

        else:
            print("Can't open port %s" % self.portName)
            return False