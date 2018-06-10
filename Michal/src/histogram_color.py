from PIL import Image
from os import remove
import numpy as np
import matplotlib.pyplot as plt
import math
import colorsys

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

    # punkt 7
    def globalSingleThreshold(self, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)
        tmp = np.empty((height, width, 3))
        tmp2 = np.empty((height, width, 3))


        #for i in range(height):
        #    for j in range(width):
        #        r, g, b = self.im[i, j]
        #        tmp[i, j] = self.RGBtoHSL((r, g, b))
        #
        #H = 0
        #n = 0
        #for i in range(height):
        #    for j in range(width):
        #        H += tmp[i, j][2]
        #        n += 1
        #H = H / n
        #
        #for i in range(height):
        #    for j in range(width):
        #        tmp2[i, j] = tmp[i, j]
        #        tmp2[i, j][2] = 0 if tmp[i, j][2] < H else 1
        #
        #for i in range(height):
        #    for j in range(width):
        #        h, s, I = tmp2[i, j]
        #        resultImage[i, j] = self.HSLtoRGB((h, s, I))

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
        self.save(resultImage, self.imName, "globalSingleThreshold")

    #punkt 5, progowanie globalne wielo-progowe
    def globalMultiThreshold(self, bins = 4, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)

        #max i min
        maxValue = [0] * 3
        minValue = [255] * 3
        #while (maxValue[0] != 255) & (maxValue[1] != 255) & (maxValue[2] != 255):
        # wartości max i min w obrazie
        for i in range(height):
            for j in range(width):
                currValue = self.im[i, j]
                for k in range(3):
                    maxValue[k] = max(maxValue[k], currValue[k])
                    minValue[k] = min(minValue[k], currValue[k])

        scale = [0] * 3
        for k in range(3):
            scale[k] = maxValue[k] / (bins - 1)

        for i in range(height):
            for j in range(width):
                pix = self.im[i, j]
                for k in range(3):
                    pix[k] = int(round(pix[k] / scale[k])) * scale[k]
                resultImage[i, j] = pix

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "globalMultiThreshold")

    # punkt 6
    def localSingleThreshold(self, dim = 3, show = False, plot = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość
        low, up = -(int(dim / 2)), (int(dim / 2) + 1)  # wsp. sąsiadów

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)
        tmp = np.empty((height, width, 3))
        tmp2 = np.empty((height, width, 3))


        #for i in range(height):
        #    for j in range(width):
        #        r, g, b = self.im[i, j]
        #        tmp[i, j] = self.RGBtoHSL((r, g, b))
        #
        #for i in range(height):
        #   for j in range(width):
        #       H = 0
        #       n = 0
        #       currPix = tmp[i, j]
        #       for iOff in range(low, up):
        #           for jOff in range(low, up):
        #               iSafe = i if ((i + iOff) > (height + low)) | ((i + iOff) < 0) else (i + iOff)
        #               jSafe = j if ((j + jOff) > (width + low)) | ((j + jOff) < 0) else (j + jOff)
        #               H += tmp[iSafe, jSafe][2]
        #               n += 1
        #       H = H / n
        #       tmp2[i, j] = currPix
        #       tmp2[i, j][2] = 0 if currPix[2] < H else 1
        #
        #for i in range(height):
        #    for j in range(width):
        #        h, s, I = tmp2[i, j]
        #        resultImage[i, j] = self.HSLtoRGB((h, s, I))



        # progowanie lokalne
        for i in range(height):
            for j in range(width):
                n = 0
                r = 0
                g = 0
                b = 0
                currPix = self.im[i, j]
                for iOff in range(low, up):
                    for jOff in range(low, up):
                        iSafe = i if ((i + iOff) > (height + low)) | ((i + iOff) < 0) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width + low)) | ((j + jOff) < 0) else (j + jOff)
                        r += int(self.im[iSafe, jSafe][0])
                        g += int(self.im[iSafe, jSafe][1])
                        b += int(self.im[iSafe, jSafe][2])
                        n += 1
                r = int(round(r / n))
                g = int(round(g / n))
                b = int(round(b / n))
                resultImage[i, j] = (0 if (currPix[0] < r) else 255, 0 if (currPix[1] < g) else 255, 0 if (currPix[2] < b) else 255)

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "localSingleThreshold")

    def localMultiThreshold(self, dim=3, bins=4, show=False, plot=False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość
        low, up = -(int(dim / 2)), (int(dim / 2) + 1)  # wsp. sąsiadów

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)

        # progowanie lokalne
        for i in range(height):
            for j in range(width):
                #print(i, j)
                n = 0
                r = 0
                g = 0
                b = 0
                currPix = self.im[i, j]
                maxValue = [0] * 3
                minValue = [255] * 3
                #while (maxValue[0] != 255) & (maxValue[1] != 255) & (maxValue[2] != 255):
                for iOff in range(low, up):
                    for jOff in range(low, up):
                        iSafe = i if ((i + iOff) > (height + low)) | ((i + iOff) < 0) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width + low)) | ((j + jOff) < 0) else (j + jOff)
                        currValue = self.im[iSafe, jSafe]
                        for k in range(3):
                            maxValue[k] = max(maxValue[k], currValue[k])
                            minValue[k] = min(minValue[k], currValue[k])
                scale = [0] * 3
                for k in range(3):
                    scale[k] = maxValue[k] / (bins - 1)
                    if scale[k] == 0:
                        scale[k] = 1
                #print("scale=", scale[0], scale[1], scale[2])
                for k in range(3):
                    #print("max=", maxValue[k], "min=", minValue[k])
                    #print("k=", k, "pix=", currPix[k], "scale=", scale[k])
                    v = int(round(currPix[k] / scale[k])) * scale[k]
                    #print("k=", k, "v=", v)
                    currPix[k] = v
                resultImage[i, j] = currPix

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.calculate(plot, resultImage)
        self.save(resultImage, self.imName, "localMultiThreshold")

    def test(self, show=True):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)
        tmp = np.empty((height, width, 3))
        tmp2 = np.empty((height, width, 3))

        for i in range(height):
            for j in range(width):
                r, g, b = self.im[i, j]
                tmp[i, j] = self.RGBtoHSI((r, g, b))

        for i in range(height):
            for j in range(width):
                h, s, I = tmp[i, j]
                resultImage[i, j] = self.HSItoRGB((h, s, I))

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "test")



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
        fileName = "img/zad6/"+ name + "_" + task + "_result.png"
        Image.fromarray(image).save(fileName)

    def RGBtoHSI(self, RGB):
        R , G, B = int(RGB[0]), int(RGB[1]), int(RGB[2])
        i = R + G + B
        I = i / (3 * 255)
        H = S = 0
        w = 0
        if (R == G) & (G == B):
            S = 0
            H = 0
        else:
            r = R / i
            g = G / i
            b = B / i
            w = 0.5 * (r - g + r - b) / math.sqrt((r - g) * (r - g) + (r - b) * (g - b))
            if w > 1:
                w = 1
            if w < - 1:
                w = -1
            H = math.acos(w)
            if B > G:
                H = 2 * math.pi - H
            S = 1 - 3 * min(r, g, b)
        H = H * 180 / math.pi
        return (H, S, I)

    def HSItoRGB(self, HSI):
        H, S, I = HSI
        R = G = B = 0
        x = I * (1 - S)
        H = H * math.pi / 180
        if H < 2 * math.pi / 3:
            y = I * (1 + (S * math.cos(H)) / math.cos(math.pi / 3 - H))
            z = 3 * I - (x + y)
            B = x
            R = y
            G = z
        elif H < 4 * math.pi / 3:
            y = I * (1 + (S * math.cos(H - 2 * math.pi / 3)) / (math.cos(math.pi / 3 - (H - 2 * math.pi / 3))))
            z = 3 * I - (x + y)
            R = x
            G = y
            B = z
        else:
            y = I * (1 + (S * math.cos(H - 4 * math.pi / 3)) / (math.cos(math.pi / 3 - (H - 4 * math.pi / 3))))
            z = 3 * I - (x + y)
            R = z
            G = x
            B = y
        return (int(round(R*255)), int(round(G*255)), int(round(B*255)))

    def RGBtoHSL(self, RGB):
        R, G, B = int(RGB[0]) / 255, int(RGB[1]) / 255, int(RGB[2]) / 255
        H, L, S = colorsys.rgb_to_hls(R, G, B)
        return (H, S, L)

    def HSLtoRGB(self, HSL):
        H, S, L = HSL[0], HSL[1], HSL[2]
        R, G, B = colorsys.hls_to_rgb(H, L, S)
        return (round(R * 255), round(G * 255), round(B * 255))

    def RGBtoIII(self, RGB):
        R, G, B = int(RGB[0]), int(RGB[1]), int(RGB[2])
        I = R * 0.34 + G * 0.33 + B * 0.33
        II = R * 0.07 + G * 0.39 - B * 0.54
        III = -R * 0.35 + G * 0.51 - B * 0.14
        return (I, II, III)

    def IIItoRGB(self, iii):
        I, II, III = iii[0], iii[1], iii[2]




