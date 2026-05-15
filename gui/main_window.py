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
        self.mixDial.valueChanged.connect(self.onMixChanged)
        self.mixLabel = QLabel(f"Mix: {self.mixDial.value()}%")
        self.mixLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.mixDial)
        layout.addWidget(self.mixLabel)
        self.setLayout(layout)

        # tone knob
        self.toneDial = QDial()
        self.toneDial.setMinimum(0)
        self.toneDial.setMaximum(100)
        self.toneDial.setValue(50)
        self.toneDial.valueChanged.connect(self.onToneChanged)
        self.toneLabel = QLabel(f"Tone: {self.toneDial.value()}%")
        self.toneLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.toneDial)
        layout.addWidget(self.toneDial)
        
        # decay knob
        # on/off switch

        self.setLayout(layout)

    def onMixChanged(self, val):
        self.reverb.mix = val / 100
        self.mixLabel.setText(f"Mix: {val}%")

    def onToneChanged(self, val):
        self.reverb.lowpass = 1.0 - (val / 100)
        for comb in self.reverb.combs:
            comb.lowpass =  self.reverb.lowpass
        self.toneLabel

class MainWindow(QMainWindow):
    def __init__(self, reverb):
        super().__init__()
        self.setWindowTitle("Guitar Effects")
        central = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(ReverbPedal(reverb))
        central.setLayout(layout)
        self.setCentralWidget(central)