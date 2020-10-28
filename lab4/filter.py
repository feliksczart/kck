import numpy as np
from skimage import io
from matplotlib import pyplot as plt
from skimage.feature import canny
from skimage.filters import median, gaussian, sobel
from skimage.morphology import disk


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
        median_img = io.imread(img)
        med = median(median_img)
        io.imshow(med)
        plt.show()

    @staticmethod
    def gaussian(img):
        gaus_img = io.imread(img)
        gaus = gaussian(gaus_img, sigma=1)
        io.imshow(gaus)
        plt.show()

    @staticmethod
    def sobel(img):
        sobel_img = io.imread(img)
        sob = sobel(sobel_img)
        io.imshow(sob)
        plt.show()

    @staticmethod
    def canny(img):
        img = io.imread(img)
        canny_mag = np.sqrt(sum([sobel(img, axis=i) ** 2
                                 for i in range(img.ndim)]) / img.ndim)

        canny_img = io.imread(canny_mag)
        can = canny(canny_img)
        io.imshow(can)
        plt.show()