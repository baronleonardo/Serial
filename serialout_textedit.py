from PyQt5.QtWidgets import QTextEdit

class SerialOut_TextEdit(QTextEdit):
    """docstring for SerialOut_TextEdit"""
    def __init__(self, parent=None):
        super(SerialOut_TextEdit, self).__init__(parent)
        self.parent = parent

    def on_serial_read(self, text):
        if type(text) is bytes:
            try:
                self.insertPlainText(text.decode('ascii'))
            except UnicodeDecodeError:
                pass

        elif type(text) is str:
            self.insertPlainTextappend(text)

    def on_autoscroll_state_changed(self, state):
        pass