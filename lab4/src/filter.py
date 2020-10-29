import numpy as np
from scipy import ndimage
from skimage import io
from matplotlib import pyplot as plt
from skimage.feature import canny
from skimage.filters import median, gaussian, sobel
from skimage.morphology import dilation, erosion


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
    def canny(): #przerobic, bo z neta
        im = np.zeros((128, 128))
        im[32:-32, 32:-32] = 1

        im = ndimage.rotate(im, 15, mode='constant')
        im = ndimage.gaussian_filter(im, 4)
        im += 0.2 * np.random.random(im.shape)

        # Compute the Canny filter for two values of sigma
        edges1 = canny(im)
        edges2 = canny(im, sigma=3)

        # display results
        plt.figure(figsize=(8, 3))

        plt.subplot(131)
        plt.imshow(im, cmap=plt.cm.jet)
        plt.axis('off')
        plt.title('noisy image', fontsize=20)

        plt.subplot(132)
        plt.imshow(edges1, cmap=plt.cm.gray)
        plt.axis('off')
        plt.title('Canny filter, $\sigma=1$', fontsize=20)

        plt.subplot(133)
        plt.imshow(edges2, cmap=plt.cm.gray)
        plt.axis('off')
        plt.title('Canny filter, $\sigma=3$', fontsize=20)

        plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                            bottom=0.02, left=0.02, right=0.98)

        plt.show()

    def dilation(img):
        dilation_img = io.imread(img)
        dil = dilation(dilation_img)
        io.imshow(dil)
        plt.show()

    def erosion(img):
        erosion_img = io.imread(img)
        ero = erosion(erosion_img)
        io.imshow(ero)
        plt.show()