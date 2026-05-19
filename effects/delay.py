import os
os.environ["SD_ENABLE_ASIO"] = "1"
import numpy as np

class Delay:
    def __init__(self, samplerate, mix=0.5, lowpass=0.5, delay_ms=500, feedback=0.5):
        self.enabled = True
        self.samplerate = samplerate
        self.mix = mix
        self.lowpass = lowpass
        self.lowpass_state = 0.0
        self.delay_ms = delay_ms
        self.delay_samples = int(delay_ms * samplerate / 1000)
        self.feedback = feedback
        self.buffer = np.zeros(int(samplerate*2)) # max 2 second delay
        self.write_pos = 0

    def set_delay(self, delay_ms):
        self.delay_ms = delay_ms    
        # convert to samples
        self.delay_samples = int(delay_ms * self.samplerate / 1000)

    def process(self, signal):
        if not self.enabled:
            return signal
        
        output = np.zeros_like(signal)
        for i in range (len(signal)):

            read_pos = (self.write_pos - self.delay_samples) % len(self.buffer) # makes sure read_pos is delay_samples behind write_pos 
            
            delayed_sample = self.buffer[read_pos]
            self.lowpass_state = delayed_sample * (1 - self.lowpass) + self.lowpass_state * self.lowpass

            output[i] = signal[i] + self.lowpass_state * self.mix
            self.buffer[self.write_pos] = signal[i] + self.lowpass_state * self.feedback

            self.write_pos = (self.write_pos + 1) % len(self.buffer)

        return output
        