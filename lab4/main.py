from filter import Filter
from loader import Load


def main():

    img = Load.img('C:/Users/czart/Desktop/Studia/kck/lab4/res/zorosanji.png')

    #Filter.gray(img)
    Filter.median(img)


if __name__ == '__main__':
    main()
