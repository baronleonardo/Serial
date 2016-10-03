from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor
import platform

class SerialOut_TextEdit(QTextEdit):
    """docstring for SerialOut_TextEdit"""
    def __init__(self, parent=None):
        super(SerialOut_TextEdit, self).__init__(parent)
        self.parent = parent

        self.OS_TYPE = platform.system()
        self.is_auto_scrolling = True

    def on_serial_read(self, text):
        if text != '\r' or self.OS_TYPE == 'Windows':
            prev_cursor_pos = self.textCursor()
            prev_v_scrollbar_pos = self.verticalScrollBar().value()
            prev_h_scrollbar_pos = self.horizontalScrollBar().value()

            self.moveCursor(QTextCursor.End)
            self.insertPlainText(text)

            if self.is_auto_scrolling is False:
                self.setTextCursor(prev_cursor_pos)
                self.verticalScrollBar().setValue(prev_v_scrollbar_pos)
                self.horizontalScrollBar().setValue(prev_h_scrollbar_pos)

            elif self.is_auto_scrolling is True:
                self.moveCursor(QTextCursor.End)
                self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())
                self.horizontalScrollBar().setValue(self.horizontalScrollBar().maximum())

    def on_autoscroll_state_changed(self, state):
        if state == Qt.Checked:
            self.is_auto_scrolling = True

        elif state == Qt.Unchecked:
            self.is_auto_scrolling = False

    def reset(self):
        self.clear()