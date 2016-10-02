from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt
import platform

class SerialOut_TextEdit(QTextEdit):
    """docstring for SerialOut_TextEdit"""
    def __init__(self, parent=None):
        super(SerialOut_TextEdit, self).__init__(parent)
        self.parent = parent

        self.__v_scrollbar = self.verticalScrollBar()
        self.cursorPositionChanged.connect(self.onCursorPositionChanged)
        self.OS_TYPE = platform.system()

    def on_serial_read(self, text):
        self.append(text)
        if text != '\r' or self.OS_TYPE == 'Windows':

    def onCursorPositionChanged(self):
        self.__v_scrollbar.setSliderPosition(self.__v_scrollbar.maximum())

    def on_autoscroll_state_changed(self, state):
        if state == Qt.Checked:
            self.cursorPositionChanged.connect(self.onCursorPositionChanged)

        elif state == Qt.Unchecked:
            self.cursorPositionChanged.disconnect(self.onCursorPositionChanged)