from os import remove

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# ZADANIE 5
class HistogramGray:
    def __init__(self, imagePath = None):
        if imagePath is not None:
            self.imName = self.getName(imagePath)
            self.im = np.array(Image.open(imagePath))

    # punkt 1
    def calculate(self, plot = False, image = None):
        if image is None:
            image = self.im

        width = image.shape[1]      # szereokść
        height = image.shape[0]     # wysokość
        hist = [0] * 256            # hostogram szarości

        for i in range(height):
            for j in range(width):
                bin = image[i, j]   # odcień szarości
                hist[bin] += 1

        if plot:
            # tablica [0, 1, ... , 254, 255]
            bins = np.arange(256)
            self.plotHistogram(bins, hist)

        return hist

    # punkt 2
    def move(self, const = 0, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        # przemieszczanie
        for i in range(height):
            for j in range(width):
                value = int(self.im[i, j]) + const
                if value < 0:
                    value = 0
                elif value > 255:
                    value = 255
                resultImage[i, j] = value

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "moveHist")

    # punkt 3
    def stretch(self, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                resultImage[i, j] = self.im[i, j]

        # rozciąganie
        maxValue = 0
        minValue = 255
        while maxValue != 255:
            # wartości max i min w obrazie
            for i in range(height):
                for j in range(width):
                    currValue = resultImage[i, j]
                    maxValue = max(maxValue, currValue)
                    minValue = min(minValue, currValue)

            # rozciąganie
            for i in range(height):
                for j in range(width):
                    pix = resultImage[i, j]
                    resultImage[i, j] = ((255 / (maxValue - minValue)) * (pix - minValue))

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "stretchHist")

    # punkt 4
    def localThreshold(self, dim = 3, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość
        l, r = -(int(round(dim / 2))), int(round(dim / 2) + 1)  # wsp. sąsiadów

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        # progowanie lokalne
        for i in range(height):
            for j in range(width):
                n = 0
                threshold = 0
                currPix = self.im[i, j]
                for iOff in range(l, r):
                    for jOff in range(l, r):
                        iSafe = i if ((i + iOff) > (height + l)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width + l)) else (j + jOff)
                        threshold += self.im[iSafe, jSafe]
                        n += 1
                threshold = int(round(threshold / n))
                resultImage[i, j] = 0 if (currPix < threshold) else 255

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "locThreshold")

    # punkt 5
    def globalThreshold(self, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        # próg globalny
        threshold = 0
        n = 0
        for i in range(height):
            for j in range(width):
                threshold += self.im[i, j]
                n += 1
        threshold = int(round(threshold / n))

        # binaryzacja
        for i in range(height):
            for j in range(width):
                resultImage[i, j] = 0 if (self.im[i, j] < threshold) else 255

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "globThreshold")





    def plotHistogram(self, bins, values):
        plt.bar(bins, values, color="gray", width=0.8)
        plt.show()

    def load(self, imagePath):
        self.imName = self.getName(imagePath)
        self.im = np.array(Image.open(imagePath))

    def getName(self, name):
        split = name.split("/")
        fileName = split[len(split) - 1]
        split = fileName.split(".")
        return split[0]

    def show(self, *image):
        size = len(image)
        for i in range(0, size):
            image[i].save("tmp.png")
            image[i].show()
        remove("tmp.png")

    def save(self, image, name, task):
        fileName = "img/zad5/" + name + "_" + task + "_result.tiff"
        Image.fromarray(image).save(fileName)
        fileName = "img/zad5/" + name + "_" + task + "_result.png"
        Image.fromarray(image).save(fileName)

    #def save(self, *image):
    #    size = len(image)
    #    for i in range(0, size):
    #        fileName = "result" + str(i + 1) + ".tiff"
    #        Image.fromarray(image[i]).save(fileName)