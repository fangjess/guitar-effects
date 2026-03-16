import os
os.environ["SD_ENABLE_ASIO"] = "1"

import sounddevice as sd

# buffer → read delayed sample → filter_state → filtered value → back into buffer
#   ↑                                                                   │
#   └───────────────────────────────────────────────────────────────────┘


class CombFilter:
    def __init__(self, delay_length, g2=0.84, lowpass=0.5): # Freeverb algorithm uses g2=0.84 and lowpass=0.5
        self.buffer = np.zeros(delay_length)
        self.g2 = g2
        self.lowpass = lowpass  # lowpass coefficient
        self.filter_state = 0.0 # previous lowpass output to be fed back into buffer
        self.write_pos = 0  # current location in the buffer

    def process(self, signal):
        

