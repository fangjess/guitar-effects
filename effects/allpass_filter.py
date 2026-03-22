import os
os.environ["SD_ENABLE_ASIO"] = "1"

import sounddevice as sd
import numpy as np

class AllpassFilter:
    def __init__(self, delay_length, feedback=0.5): # Freeverb uses 0.5 instead of the golden ratio reciprocal
        self.buffer = np.zeros(delay_length)
        self.write_pos = 0
        self.feedback = feedback

    def process(self, signal):
        output = np.zeros_like(signal)
        
        for i in range(len(signal)):
            output[i] = self.buffer[self.write_pos] - signal[i]
            self.buffer[self.write_pos] = signal[i] + self.buffer[self.write_pos] * self.feedback
            self.write_pos = (self.write_pos + 1) % len(self.buffer)

        return output