from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ReverbPedal(QWidget):
    def __init__(self, reverb):
        super().__init__()
        self.reverb = reverb
        self.pedal_ui()

    def pedal_ui(self):
        layout = QVBoxLayout()

        # title
        titleLabel = QLabel("REVERB")
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titleLabel)

        # mix knob
        self.mixDial = QDial()
        self.mixDial.setMinimum(0)
        self.mixDial.setMaximum(100)
        self.mixDial.setValue(30) # because in freeverb init: mix = 0.3
        self.mixLabel = QLabel(f"Mix: {self.mixDial.value()}%")
        self.mixLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mixDial.valueChanged.connect(self.onMixChanged)
        layout.addWidget(self.mixDial)
        layout.addWidget(self.mixLabel)
        self.setLayout(layout)
        # tone knob
        # decay knob
        # on/off switch

    def onMixChanged(self, val):
        self.reverb.mix = val/100
        self.mixLabel.setText(f"Mix: {val}%")

class MainWindow(QMainWindow):
    def __init__(self, reverb):
        super().__init__()
        self.setWindowTitle("Guitar Effects")
        central = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(ReverbPedal(reverb))
        central.setLayout(layout)
        self.setCentralWidget(central)