import os
os.environ["SD_ENABLE_ASIO"] = "1"

class Delay:
    def __init__(self, samplerate, mix=0.5, lowpass=0.5, delay_time=300, feedback=0.5):
        self.samplerate = samplerate
        self.mix = mix
        self.lowpass = lowpass
        self.lowpass_state = 0.0
        self.feedback = feedback