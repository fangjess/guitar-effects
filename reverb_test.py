import os
os.environ["SD_ENABLE_ASIO"] = "1"
import sounddevice as sd
from PyQt6.QtWidgets import QApplication
from effects.freeverb import Freeverb
from gui.main_window import MainWindow

# my settings
SAMPLE_RATE = 48000
BUFFER_SIZE = 256
DEVICE = 12

reverb = Freeverb(g2=0.84, lowpass=0.5, mix=0.3, samplerate=SAMPLE_RATE)

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    signal = indata[:, 1].copy()  # channel 1 for guitar input on my driver
    output = reverb.process(signal)
    outdata[:, 0] = output
    outdata[:, 1] = output

app = QApplication([])
window = MainWindow(reverb)
window.show()

stream = sd.Stream(device=(DEVICE, DEVICE),        # (input_index, output_index), 12 for ASIO in/out for me
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