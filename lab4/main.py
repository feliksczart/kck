from filter import Filter
from loader import Load


def main():
    img = Load.img('res/dem.jpg')
    # io.imshow(img)
    # plt.show()

    # Filter.gray(img)
    # Filter.median(img)
    # Filter.gaussian(img)
    # Filter.sobel(img)
    Filter.canny(img)


if __name__ == '__main__':
    main()
