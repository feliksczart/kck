from __future__ import division
from pylab import *
from numpy import *
from scipy import *
from ipywidgets import *
import math as mt
import random
import scipy.io.wavfile
import sys, getopt, os
import warnings

warnings.simplefilter("ignore")

def load_file(f):

    (sampling, signal) = scipy.io.wavfile.read(str(f))
    print(sampling)
    print(signal)

def expect(dir):
    expectations = []
    for filename in sorted(os.listdir(dir)):
        if filename.endswith('.wav'):
            fil = filename.split('_')
            fill = fil[1].split('.')
            KM = fill[0]
            expectations.append(KM)
            (sampling, signal) = scipy.io.wavfile.read(dir+'/'+filename)
    return expectations

def check():

    expectations = expect('trainall')
    #bedziemy wprowadzać uzyskane przez nas wyniki do tej listy
    our_whole_output = ['K', 'M', 'K', 'M', 'M', 'K', 'M', 'K', 'K', 'M', 'M', 'K', 'M', 'K', 'K', 'K', 'M', 'K', 'M', 'M', 'M', 'K', 'M', 'M', 'K', 'M', 'M', 'K', 'K', 'M', 'K', 'M', 'M', 'K', 'M', 'K', 'K', 'M', 'M', 'K', 'K', 'M', 'M', 'K', 'M', 'K', 'K', 'K', 'M', 'K', 'K', 'M', 'M', 'K', 'K', 'M', 'K', 'M', 'K', 'K', 'M', 'K', 'M', 'M', 'M', 'K', 'K', 'K', 'K', 'M', 'M', 'K', 'K', 'K', 'M', 'M', 'K', 'M', 'K', 'M', 'K', 'M', 'K', 'M', 'K', 'K', 'M', 'K', 'M', 'M', 'M']

    good = 0
    for i in range(len(expectations)):
        if our_whole_output[i] == expectations[i]:
            good += 1
    
    print()
    print('Skuteczność działania naszego programu wynosi: '+str(good/len(expectations)*100)+'%')

if __name__ == "__main__":
    load_file(sys.argv[1])
    check()