# Guitar Effects Processor
A real-time guitar effects processor built in Python. Audio is captured from an audio interface, processed through a signal chain, and output with near-zero latency using ASIO drivers.

## Built With
- Python
- NumPy / SciPy
- SoundDevice (PortAudio/ASIO)
- PyQt6

## Implemented
Reverb: Reverb (freeverb algorithm) implemented with 8 parallel comb filters, single pole lowpass damping and 4 series allpass filters

## In Progress
- Delay
- Amp Sim
- GUI
- Tuner
