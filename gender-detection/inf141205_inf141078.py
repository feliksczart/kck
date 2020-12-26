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
    duration = float(samples_count)/sampling
    if not isinstance(signal[0], np.int16):
      signal = [s[0] for s in signal]
    signal = signal * kaiser(samples_count, 100)

    spectrum = np.log(abs(np.fft.rfft(signal)))
    hps = copy(spectrum)
    for h in np.arange(2, 6):
      dec = decimate(spectrum, h)
      hps[:len(dec)] += dec
    peak_start = 50 * duration
    peak = np.argmax(hps[int(peak_start):])
    fundamental = (peak_start + peak) / duration

    if fundamental <= 175:
      gender = 'M'
    elif fundamental > 175:
      gender = 'K'
    else:
      gender = '-'

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
          
def check(our_results):
    expectations = expect('trainall')
    good = 0
    for i in range(len(expectations)):
        if our_results[i] == expectations[i]:
            good += 1
    
    print()
    print('Skuteczność działania naszego programu wynosi: '+str(good/len(expectations)*100)+'%')

if __name__ == "__main__":
    # sampling, signal = load_file(sys.argv[1])
    # gender = detect_gender(sampling,signal)
    # print(gender)

    # Sprawdzenie skuteczności naszego programu
    results = our_results('trainall')
    check(results)