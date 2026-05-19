import os
os.environ["SD_ENABLE_ASIO"] = "1"

import sounddevice as sd
import numpy as np
from PyQt6.QtWidgets import QApplication
from effects.freeverb import Freeverb
from effects.delay import Delay
from gui.main_window import MainWindow

SAMPLE_RATE = 48000
BUFFER_SIZE = 256
DEVICE = 12

reverb = Freeverb(g2=0.84, lowpass=0.5, mix=0.3, samplerate=SAMPLE_RATE)
delay = Delay(samplerate=SAMPLE_RATE, mix=0.5, delay_ms=500, feedback=0.5)

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    signal = indata[:, 1].copy()
    signal = delay.process(signal)
    signal = reverb.process(signal)
    outdata[:, 0] = signal
    outdata[:, 1] = signal

app = QApplication([])
window = MainWindow(reverb, delay)
window.show()

stream = sd.Stream(device=(DEVICE, DEVICE),
                   samplerate=SAMPLE_RATE,
                   blocksize=BUFFER_SIZE,
                   dtype='float32',
                   channels=(2, 2),
                   latency='low',
                   callback=callback)
stream.start()
app.exec()
stream.stop()
stream.close()