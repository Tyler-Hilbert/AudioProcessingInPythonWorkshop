import sys
sys.path.insert(0, 'ThinkDSP/code/') 
import thinkdsp
import matplotlib.pyplot as pyplot

# Read in audio file
# FIXME - will this work for non wav files
wave = thinkdsp.read_wave('test.wav')

# Grab first 10 seconds of audio (you can ignore me)
clipLength = 10 # in seconds
index = 0
while (index < wave.ts.size and wave.ts[index] < clipLength):
	index += 1
# Remove extras
wave.ts = wave.ts[:index]
wave.ys = wave.ys[:index]


# Filter
spectrum = wave.make_spectrum()
spectrum.low_pass(cutoff = 500, factor = .1)
#spectrum.high_pass(cutoff = 1500, factor = .01)
filteredWave = spectrum.make_wave()


# Play filtered audio file
filteredWave.play()


# Plot spectrum of audio file
spectrum = filteredWave.make_spectrum()
spectrum.plot()
pyplot.show()
