from matplotlib import pyplot as plt
from skimage import io

from filter import Filter
from loader import Load


def main():

    img = Load.img('C:/Users/czart/Desktop/Studia/kck/lab4/res/zorosanji.png')
    #io.imshow(img)
    #plt.show()

    #Filter.gray(img)
    #Filter.median(img)
    Filter.gaussian(img)


if __name__ == '__main__':
    main()
