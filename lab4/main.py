from skimage import io
from filter import Filter
from loader import Load
from matplotlib import pyplot as plt


def main():
    img = Load.img('res/zorosanji.png')
    io.imshow(img)
    plt.show()

    # Filter.gray(img)
    # Filter.median(img)
    # Filter.gaussian(img)
    # Filter.sobel(img)
    # Filter.canny()
    # Filter.dilation(img)
    # Filter.erosion(img)


if __name__ == '__main__':
    main()
