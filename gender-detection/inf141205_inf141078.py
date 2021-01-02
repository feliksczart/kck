from __future__ import division
from pylab import *
from numpy import *
from scipy import *
from ipywidgets import *
import math as mt
import random
import scipy.io.wavfile
from scipy.signal import kaiser, decimate
import sys, getopt, os
import warnings

warnings.simplefilter("ignore")

def load_file(f):
    (sampling, signal) = scipy.io.wavfile.read(str(f))
    return sampling, signal

def detect_gender(sampling, signal):
    
    samples_count = len(signal)
    duration = samples_count/sampling
    
    if not isinstance(signal[0], np.int16):
      signal = [s[0] for s in signal]
                      #Bessel function
    signal = signal * kaiser(samples_count, 100)

    spectrum = np.log(abs(fft.rfft(signal)))
    spectrum_cp = copy(spectrum)
    
    for i in arange(2, 5):
          #Downsample the signal after applying an anti-aliasing filter
      d = decimate(spectrum, i)
      spectrum_cp[:len(d)] += d

    peak_begin = int(90 * duration)
    peak = argmax(spectrum_cp[peak_begin:])
    fundamental_frequency = (peak_begin + peak) / duration
    #Male between 85 - 180 Hz, Female between 165 - 255 Hz

    if fundamental_frequency <= 172.5:
      gender = 'M'
    else:
      gender = 'K'

    return gender

def expect(dir):
    expectations = []
    for filename in sorted(os.listdir(dir)):
        if filename.endswith('.wav'):
            fil = filename.split('_')
            fill = fil[1].split('.')
            KM = fill[0]
            expectations.append(KM)
    return expectations

def our_results(dir):
    results = []
    for filename in sorted(os.listdir(dir)):
        if filename.endswith('.wav'):
            (sampling, signal) = load_file(dir+'/'+filename)
            gender = detect_gender(sampling,signal)
            results.append(gender)

    return results
          
def check(our_results,dir):
    expectations = expect(dir)
    good = 0
    for i in range(len(expectations)):
        if our_results[i] == expectations[i]:
            good += 1
    
    print()
    print('Skuteczność działania naszego programu wynosi: '+str(good/len(expectations)*100)+'%')

if __name__ == "__main__":
    sampling, signal = load_file(sys.argv[1])
    gender = detect_gender(sampling,signal)
    print(gender)

    # Sprawdzenie skuteczności naszego programu
    
    # results = our_results('trainall')
    # check(results,'trainall')