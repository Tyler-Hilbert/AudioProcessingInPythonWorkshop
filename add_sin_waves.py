import sys
sys.path.insert(0, 'ThinkDSP/code/') 
import thinkdsp
import matplotlib.pyplot as pyplot

# Generate wave
sin1 = thinkdsp.SinSignal(freq=400, amp=0.5)
sin2 = thinkdsp.SinSignal(freq=800, amp=0.3)
mix = sin1 + sin2 # Notice here how 2 waves can be added together
wave = mix.make_wave(duration=2, start=0, framerate=44100)

# Play wave
wave.play()

# Plot wave
period = mix.period
segment = wave.segment(start=0, duration=period*3)
segment.plot()
pyplot.show()

