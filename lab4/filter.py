from skimage import io
from matplotlib import pyplot as plt
from skimage.filters import median, gaussian
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