from PyQt5.QtWidgets import QPushButton

class PauseGraphButton(QPushButton):
    def __init__(self, parent=None):
        super(PauseGraphButton, self).__init__(parent)
        self.parent = parent

    def on_toggle(self, state):
        if state is True:
            self.setText("Resume")
        else:
            self.setText("Pause")