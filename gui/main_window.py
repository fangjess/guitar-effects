from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class ReverbPedal(QWidget):
    def __init__(self, reverb):
        super().__init__()
        self.reverb = reverb
        self.pedal_ui()

    def pedal_ui(self):
        reverbBox = QGroupBox("REVERB")
        reverbBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout = QVBoxLayout()

        # title
        # titleLabel = QLabel("REVERB")
        # titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # layout.addWidget(titleLabel)

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

        # knob layout
        parameters = QHBoxLayout()

        # tone knob
        toneBox = QVBoxLayout()
        self.toneDial = QDial()
        self.toneDial.setMinimum(0)
        self.toneDial.setMaximum(100)
        self.toneDial.setValue(50)
        self.toneDial.valueChanged.connect(self.onToneChanged)
        self.toneLabel = QLabel(f"Tone: {self.toneDial.value()}%")
        self.toneLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        toneBox.addWidget(self.toneDial)
        toneBox.addWidget(self.toneLabel)
        
        # decay knob
        decayBox = QVBoxLayout()
        self.decayDial = QDial()
        self.decayDial.setMinimum(0)
        self.decayDial.setMaximum(99)
        self.decayDial.setValue(84)
        self.decayDial.valueChanged.connect(self.onDecayChanged)
        self.decayLabel = QLabel(f"Decay: {self.decayDial.value()}%")
        self.decayLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        decayBox.addWidget(self.decayDial)
        decayBox.addWidget(self.decayLabel)

        parameters.addLayout(toneBox)
        parameters.addLayout(decayBox)
        layout.addLayout(parameters)

        # power switch
        self.powerSwitch = QPushButton("ON")
        self.powerSwitch.setCheckable(True)
        self.powerSwitch.setChecked(True)
        self.powerSwitch.toggled.connect(self.onPowerToggled)
        layout.addWidget(self.powerSwitch)

        reverbBox.setLayout(layout)
        outerLayout = QVBoxLayout()
        outerLayout.addWidget(reverbBox)
        self.setLayout(outerLayout)

    def onMixChanged(self, val):
        self.reverb.mix = val / 100
        self.mixLabel.setText(f"Mix: {val}%")

    def onToneChanged(self, val):
        self.reverb.lowpass = 1.0 - (val / 100)
        for comb in self.reverb.combs:
            comb.lowpass = self.reverb.lowpass
        self.toneLabel.setText(f"Tone: {val}%")

    def onDecayChanged(self, val):
        g2 = val / 100
        self.reverb.g2 = g2
        for comb in self.reverb.combs:
            comb.g2 = g2
        self.decayLabel.setText(f"Decay: {val}%")

    def onPowerToggled(self, checked):
        self.reverb.enabled  = checked
        self.powerSwitch.setText("ON" if checked else "OFF")


class MainWindow(QMainWindow):
    def __init__(self, reverb):
        super().__init__()
        self.setWindowTitle("Guitar Effects")
        central = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(ReverbPedal(reverb))
        central.setLayout(layout)
        self.setCentralWidget(central)