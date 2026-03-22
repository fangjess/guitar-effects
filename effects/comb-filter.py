import os
os.environ["SD_ENABLE_ASIO"] = "1"

import sounddevice as sd
import numpy as np

# buffer → read delayed sample → filter_state → filtered value → back into buffer
#   ↑                                                                   │
#   └───────────────────────────────────────────────────────────────────┘


class CombFilter:
    def __init__(self, delay_length, g2=0.84, lowpass=0.5): # Freeverb algorithm uses g2=0.84 and lowpass=0.5, delay_length is number of samples between read/write
        self.buffer = np.zeros(delay_length)
        self.g2 = g2    # decays amplitude over time
        self.lowpass = lowpass  # lowpass coefficient
        self.lowpass_state = 0.0 # more lowpass each cycle; this remembers how much lowpass to apply each cycle to gradually dampen
        self.write_pos = 0  # current location in the buffer

    def process(self, signal):
        output = np.zeros_like(signal) 

        # fill output array
        for i in range (len(signal)):

            read_pos = self.write_pos
            output[i] = self.buffer[read_pos]

            self.lowpass_state = output[i] * (1 - self.lowpass) + self.lowpass_state * self.lowpass
            self.buffer[self.write_pos] = signal[i] + self.lowpass_state * self.g2

            self.write_pos = (self.write_pos + 1) % len(self.buffer)

        return output

