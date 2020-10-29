from skimage import io

from src.filter import Filter
from src.loader import Load
from matplotlib import pyplot as plt
#test git to drive2

def main():
    img = Load.img('samolot00.jpg')
    #io.imshow(img)
    #plt.show()

    # Filter.gray(img)
    # Filter.median(img)
    # Filter.gaussian(img)
    # Filter.sobel(img)
    # Filter.canny()
    # Filter.dilation(img)
    # Filter.erosion(img)
    Filter.contur3(img)


if __name__ == '__main__':
    main()
