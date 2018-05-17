from PIL import Image
from os import remove
import numpy as np
import matplotlib.pyplot as plt
import math

# ZADANIE 6
class HistogramColor:
    def __init__(self, imagePath = None):
        if imagePath is not None:
            self.imName = self.getName(imagePath)
            self.im = np.array(Image.open(imagePath))

    # punkt 1
    def calculate(self, plot = False, image = None):
        if image is None:
            image = self.im

        width = image.shape[1]      # szerokość
        height = image.shape[0]     # wysokość
        hist = [0] * 3              # histogram RGB
        hist[0] = [0] * 256         # histogram R
        hist[1] = [0] * 256         # histogram G
        hist[2] = [0] * 256         # histogram B

        for i in range(height):
            for j in range(width):
                bin = image[i, j]
                for k in range(3):
                    hist[k][bin[k]] += 1

        if plot:
            # tablica [0, 1, ... , 254, 255]
            bins = np.arange(256)
            self.plotHistogram(bins, hist)

        return hist                 # [0] - hist R, [1] - hist G, [2] - hist B

    # punkt 2
    def move(self, const = 0, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)

        # przemieszczanie
        for i in range(height):
            for j in range(width):
                value = self.im[i, j]
                for k in range(len(value)):
                    v = value[k]
                    v += const
                    if v < 0:
                        v = 0
                    elif v > 255:
                        v = 255
                    value[k] = v
                resultImage[i, j] = value

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "moveHist")

    # punkt 3
    def stretch(self, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                resultImage[i, j] = self.im[i, j]

        # rozciąganie
        maxValue = [0] * 3
        minValue = [255] * 3
        while (maxValue[0] != 255) & (maxValue[1] != 255) & (maxValue[2] != 255):
            # wartości max i min w obrazie
            for i in range(height):
                for j in range(width):
                    currValue = resultImage[i, j]
                    for k in range(3):
                        maxValue[k] = max(maxValue[k], currValue[k])
                        minValue[k] = min(minValue[k], currValue[k])

            # rozciąganie
            for i in range(height):
                for j in range(width):
                    pix = resultImage[i, j]
                    for k in range(3):
                        pix[k] = ((255 / (maxValue[k] - minValue[k])) * (pix[k] - minValue[k]))
                    resultImage[i, j] = pix

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "stretchHist")

    # punkt 4, progowanie 1-progowe
    def monoThresholding(self, threshold = 127, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)

        # binaryzacja
        for i in range(height):
            for j in range(width):
                r = 0 if (self.im[i, j][0] < threshold) else 255
                g = 0 if (self.im[i, j][1] < threshold) else 255
                b = 0 if (self.im[i, j][2] < threshold) else 255
                resultImage[i, j] = (r, g, b)

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "monoThresh")

    #punkt 5, progowanie wielo-progowe
    def poliThresholding(self, bins = 4, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)

        scale = 256 / bins
        scale = math.floor(scale * 10) / 10

        # kwantyzacja każdego kanału
        for i in range(height):
            for j in range(width):
                r = int(self.im[i, j][0] / scale) * scale
                g = int(self.im[i, j][1] / scale) * scale
                b = int(self.im[i, j][2] / scale) * scale
                resultImage[i, j] = (r, g, b)

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "multiThresh")

    # punkt 6 ?????????
    def localThreshold(self, dim = 3, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość
        l, r = -(int(round(dim / 2))), int(round(dim / 2) + 1)  # wsp. sąsiadów

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)

        # progowanie lokalne
        for i in range(height):
            for j in range(width):
                n = 0
                r = 0
                g = 0
                b = 0
                currPix = self.im[i, j]
                for iOff in range(l, r):
                    for jOff in range(l, r):
                        iSafe = i if ((i + iOff) > (height + l)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width + l)) else (j + jOff)
                        r += self.im[iSafe, jSafe][0]
                        g += self.im[iSafe, jSafe][1]
                        b += self.im[iSafe, jSafe][2]
                        n += 1
                r = int(round(r / n))
                g = int(round(g / n))
                b = int(round(b / n))
                resultImage[i, j] = (0 if (currPix[0] < r) else 255, 0 if (currPix[1] < g) else 255, 0 if (currPix[2] < b) else 255)

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "locThreshold")

    # punkt 7
    def globalThreshold(self, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)

        # próg globalny
        globalR = 0
        globalG = 0
        globalB = 0
        nR = 0
        nG = 0
        nB = 0
        for i in range(height):
            for j in range(width):
                globalR += self.im[i, j][0]
                nR += 1
                globalG += self.im[i, j][1]
                nG += 1
                globalB += self.im[i, j][2]
                nB += 1
        globalR = int(round(globalR / nR))
        globalG = int(round(globalG / nG))
        globalB = int(round(globalB / nB))

        # kwantzyacja
        for i in range(height):
            for j in range(width):
                resultImage[i, j] = (0 if (self.im[i, j][0] < globalR) else 255, 0 if (self.im[i, j][1] < globalG) else 255, 0 if (self.im[i, j][2] < globalB) else 255)

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "globThreshold")





    def plotHistogram(self, bins, values):
        fig = plt.figure()
        plt.subplot(2, 2, 1)
        plt.bar(bins - 0.33, values[0], color="red", width=0.33)
        plt.title("red")
        plt.ylabel("number of accurences")

        plt.subplot(2, 2, 2)
        plt.bar(bins, values[1], color="green", width=0.33)
        plt.title("green")

        plt.subplot(2, 2, 3)
        plt.bar(bins + 0.33, values[2], color="blue", width=0.33)
        plt.xlabel("blue")
        plt.ylabel("number of accurences")

        plt.subplot(2, 2, 4)
        plt.bar(bins - 0.33, values[0], color="red", width=0.33)
        plt.bar(bins, values[1], color="green", width=0.33)
        plt.bar(bins + 0.33, values[2], color="blue", width=0.33)
        plt.xlabel("RGB")
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
        fileName = "img/zad6/"+ name + "_" + task + "_result.tiff"
        Image.fromarray(image).save(fileName)

    #def save(self, *image):
    #    size = len(image)
    #    for i in range(0, size):
    #        fileName = "result" + str(i + 1) + ".tiff"
    #        Image.fromarray(image[i]).save(fileName)