import os
from skimage import data_dir, io
from matplotlib import pyplot as plt


class Load:
    def __init__(self):
        return

    @staticmethod
    def img(file):
        img = os.path.join('C:/Users/czart/Desktop/Studia/kck/lab4/', file)
        return img
