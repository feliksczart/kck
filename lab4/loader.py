import os
from skimage import data_dir, io
from matplotlib import pyplot as plt


class Load:
    def __init__(self):
        return

    @staticmethod
    def img(file):
        img = os.path.join(data_dir, file)
        io.imshow(img)
        plt.show()

    @staticmethod
    def img_gray(file):
        img = os.path.join(data_dir, file)
        gray_img = io.imread(img,as_gray=True)
        io.imshow(gray_img)
        plt.show()
