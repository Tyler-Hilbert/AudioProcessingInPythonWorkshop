# This file shows how to generate a sine wave using the ThinkDSP library.
import sys
sys.path.insert(0, 'ThinkDSP/code/') 
import thinkdsp
import matplotlib.pyplot as pyplot

# Generate wave
sin = thinkdsp.SinSignal(freq=400, amp=0.5) # Where freq is the frequency and amp is the amplitude of the sine wave
wave = sin.make_wave(duration=2, start=0, framerate=44100) # Turn the sin wave into an audio wave

# Play wave
wave.play()

# Plot wave
period = sin.period
segment = wave.segment(start=0, duration=period*3)
segment.plot()
pyplot.show()

