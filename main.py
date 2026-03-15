import os
os.environ["SD_ENABLE_ASIO"] = "1"

import sounddevice as sd


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    guitar = indata[:, 1]  # channel 1 = input 2 on your interface
    outdata[:, 0] = guitar
    outdata[:, 1] = guitar

with sd.Stream(device=(12, 12),        # (input_index, output_index) this specifies what input/output device
               samplerate=48000,
               blocksize=256,
               dtype='float32',
               channels=(2, 2),
               latency='low',
               callback=callback):
    print("Running... press Enter to stop")
    input()  # blocks here until you hit Enter