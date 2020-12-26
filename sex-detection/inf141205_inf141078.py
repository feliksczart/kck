from __future__ import division
from pylab import *
from numpy import *
from scipy import *
from ipywidgets import *
import math as mt
import random
import scipy.io.wavfile
import sys, getopt
import warnings

warnings.simplefilter("ignore")

def load_file(f):

    (sampling, signal) = scipy.io.wavfile.read(str(f))
    print(sampling)
    print(signal)

if __name__ == "__main__":
    load_file(sys.argv[1])