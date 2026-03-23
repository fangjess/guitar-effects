import os
os.environ["SD_ENABLE_ASIO"] = "1"
import sounddevice as sd
import numpy as np
from .comb_filter import CombFilter
from .allpass_filter import AllpassFilter

COMB_DELAYS = [1116, 1188, 1277, 1356, 1422, 1491, 1557, 1617] # Jezar's values: https://ccrma.stanford.edu/~jos/pasp/Schroeder_Reverberators.html
ALLPASS_DELAYS = [556, 441, 341, 225]
SAMPLE_REF = 44100

class Freeverb:
    def __init__(self, g2=0.84, lowpass=0.5, mix=0.3, samplerate=48000):
        self.mix = mix
        self.g2 = g2
        self.lowpass = lowpass
        scale = samplerate / SAMPLE_REF

        self.combs = [
            CombFilter(int(i * scale), g2=g2, lowpass=lowpass)
            for i in COMB_DELAYS
        ]
        self.allpasses = [
            AllpassFilter(int(i * scale))
            for i in ALLPASS_DELAYS
        ]

    def process(self, signal):
        dry = signal.copy()
        wet = sum(c.process(signal) for c in self.combs) # sums together output of each comb running in parallel
        wet *= 0.125 # prevent clipping

        for a in self.allpasses: # allpass filters applied in series
            wet = a.process(wet)

        return dry * (1 - self.mix) + wet * self.mix