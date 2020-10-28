from skimage import io
from matplotlib import pyplot as plt
from skimage.filters import median
import numpy as np


class Filter:
    def __init__(self):
        return

    @staticmethod
    def gray(img):
        gray_img = io.imread(img, as_gray=True)
        io.imshow(gray_img)
        plt.show()

    @staticmethod
    def median(img):
        median_img = median(img, selem=np.ones((5, 5)))
        io.imshow(median_img)
        plt.show()
