# Guitar Effects Processor
A real-time guitar effects processor built in Python. Instrument signal is captured from an audio interface and processed through a signal chain.

*Note*: The device number is hardcoded to mine and you will have to query your own input/output devices and change main.py accordingly. Won't work in a DAW yet.<br>
``python -c "import os; os.environ['SD_ENABLE_ASIO'] = '1'; import sounddevice as sd; print(sd.query_devices())"``

## Built With
- Python
- NumPy / SciPy
- SoundDevice (PortAudio/ASIO)
- PyQt6

## Implemented
Reverb: Reverb (freeverb algorithm) implemented with 8 parallel comb filters, single pole lowpass damping and 4 series allpass filters

## Demo Video
Make sure sound is on!<br>


https://github.com/user-attachments/assets/af16815f-d47a-4bea-adb5-d011df315f94



## What I learned
This document compiles all the questions I had during research and development in order to give a more in-depth explanation of how the application works, and to explain why I made some choices and what I learned from this project. Will be updated as the project continues.
- Link to Google Doc: [Guitar Effects Processor: What I Learned](https://docs.google.com/document/d/1cyYXkWK0o02uTQZqrJiAEZFEgrTdHcW12-cJh3hBqyA/edit?usp=sharing)

In summary:
- Processing sound waves using math translated into code
- Handling audio input/output with sounddevice
- Coding in Python with PyQt6

## To add in the future:
- VST/DAW compatibility
- Tempo-synced delay
- Amp Sim
- GUI
- Tuner

## Project Wireframe
<img width="1179" height="707" alt="GUITAR EFFECTS APP WIREFRAME" src="https://github.com/user-attachments/assets/de16da3d-1b9c-4fd0-8365-4315c69dd281" />
Made using Figma

## Sources
- [Introduction to Audio Filters](https://ccrma.stanford.edu/~jos/filters/) by Julius O. Smith III
- [PyQt6 Widgets](https://www.pythonguis.com/tutorials/pyqt6-widgets/) by Martin Fitzpatrick
- Understanding algorithmic concepts and syntax with help from [Claude by Anthropic](https://claude.ai/new)
