from PIL import Image
from os import remove
import numpy as np
import matplotlib.pyplot as plt
import math
import colorsys

# ZADANIE 9
class Filter:
    def __init__(self, imagePath = None):
        if imagePath is not None:
            self.imName = self.getName(imagePath)
            self.im = np.array(Image.open(imagePath))

    # punkt 1, lowpass 1
    def averageColor(self, show = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)
                                    #       [1, 1, 1]
        mask = np.ones((3, 3))      # 1/9 * [1, 1, 1]
                                    #       [1, 1, 1]
        # wygładzanie
        for i in range(height):
            for j in range(width):
                avgr = 0
                avgg = 0
                avgb = 0
                n = 0
                for iOff in range(-1, 1):
                    for jOff in range(-1, 1):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        avgr += self.im[iSafe, jSafe][0] * mask[iOff + 1, jOff + 1]
                        avgg += self.im[iSafe, jSafe][1] * mask[iOff + 1, jOff + 1]
                        avgb += self.im[iSafe, jSafe][2] * mask[iOff + 1, jOff + 1]
                        n += mask[iOff + 1, jOff + 1]
                avgr = int(round(avgr / n))
                avgg = int(round(avgg / n))
                avgb = int(round(avgb / n))
                resultImage[i, j] = (avgr, avgg, avgb)

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "lowpassAvg")

    # punkt 1, lowpass 1
    def averageGray(self, show = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)
                                    #       [1, 1, 1]
        mask = np.ones((3, 3))      # 1/9 * [1, 1, 1]
                                    #       [1, 1, 1]
        # wygładzanie
        for i in range(height):
            for j in range(width):
                avg = 0
                n = 0
                for iOff in range(-1, 1):
                    for jOff in range(-1, 1):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        avg += self.im[iSafe, jSafe] * mask[iOff + 1, jOff + 1]
                        n += mask[iOff + 1, jOff + 1]
                avg = int(round(avg / n))
                resultImage[i, j] = avg

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.save(resultImage, self.imName, "lowpassAvg")

    #punkt 1, lowpass 2
    def gaussColor(self, show = False):
        width = self.im.shape[1]    # szereokść
        height = self.im.shape[0]   # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)

        mask = np.ones((5, 5))                                  #        [1, 1, 1, 1, 1]
        mask[1, 1] = mask[3, 3] = mask[1, 3] = mask[3, 1] = 4   #        [1, 4, 6, 4, 1]
        mask[1, 2] = mask[3, 2] = 6                             # 1/47 * [1, 1, 1, 1, 1]
                                                                #        [1, 4, 6, 4, 1]
        # filtering                                             #        [1, 1, 1, 1, 1]
        for i in range(height):
            for j in range(width):
                n = 0
                r, g, b = 0, 0, 0
                for iOff in range(-2, 3):
                    for jOff in range(-2, 3):
                        iSafe = i if ((i + iOff) > (height - 2)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 2)) else (j + jOff)
                        r += self.im[iSafe, jSafe][0] * mask[iOff + 2, jOff + 2]
                        g += self.im[iSafe, jSafe][1] * mask[iOff + 2, jOff + 2]
                        b += self.im[iSafe, jSafe][2] * mask[iOff + 2, jOff + 2]
                        n += mask[iOff + 2, jOff + 2]
                r = int(round(r / n))
                g = int(round(g / n))
                b = int(round(b / n))
                resultImage[i, j] = (r, g, b)

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "lowpassGauss")

    # punkt 1, lowpass 2
    def gaussGray(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        mask = np.ones((5, 5))                                   #        [1, 1, 1, 1, 1]
        mask[1, 1] = mask[3, 3] = mask[1, 3] = mask[3, 1] = 4    #        [1, 4, 6, 4, 1]
        mask[1, 2] = mask[3, 2] = 6                              # 1/47 * [1, 1, 1, 1, 1]
                                                                 #        [1, 4, 6, 4, 1]
                                                                 #        [1, 1, 1, 1, 1]

        # filtering
        for i in range(height):
           for j in range(width):
               n = 0
               value = 0
               for iOff in range(-2, 3):
                   for jOff in range(-2, 3):
                       iSafe = i if ((i + iOff) > (height - 2)) else (i + iOff)
                       jSafe = j if ((j + jOff) > (width - 2)) else (j + jOff)
                       value += self.im[iSafe, jSafe] * mask[iOff + 2, jOff + 2]
                       n += mask[iOff + 2, jOff + 2]
               value = int(round(value / n))
               resultImage[i, j] = value

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.save(resultImage, self.imName, "lowpassGauss")

    # punkt 2, highpass 1
    def robertsColor(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)
        tmp = np.empty((height, width, 3))
        tmp2 = np.empty((height, width, 3))

        mask = np.zeros((3, 3))     # [0, 0, 0]
        mask[2, 1] = 1              # [0, 0,-1]
        mask[1, 2] = -1             # [0, 1, 0]

        # filtracja
        for i in range(height):
            for j in range(width):
                r, g, b = 0, 0, 0
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        r += self.im[iSafe, jSafe][0] * mask[iOff + 1, jOff + 1]
                        g += self.im[iSafe, jSafe][1] * mask[iOff + 1, jOff + 1]
                        b += self.im[iSafe, jSafe][2] * mask[iOff + 1, jOff + 1]
                resultImage[i, j] = (abs(r), abs(g), abs(b))

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "highpassRoberts")

    # punkt 2, highpass 1
    def robertsGray(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        mask = np.zeros((3, 3))     # [0, 0, 0]
        mask[2, 1] = 1              # [0, 0,-1]
        mask[1, 2] = -1             # [0, 1, 0]

        # filtracja
        for i in range(height):
            for j in range(width):
                value = 0
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        value += self.im[iSafe, jSafe] * mask[iOff + 1, jOff + 1]
                resultImage[i, j] = abs(value)

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.save(resultImage, self.imName, "highpassRoberts")

    # punkt 2, highpass 2
    def prewittColor(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)
        tmp = np.empty((height, width, 3))
        tmp2 = np.empty((height, width, 3))

        mask = np.zeros((3, 3))                               # [-1, 0, 1]
        mask[0, 0] = mask[1, 0] = mask[2, 0] = -1             # [-1, 0, 1]
        mask[0, 2] = mask[1, 2] = mask[2, 2] = 1              # [-1, 0, 1]

        # filtracja
        for i in range(height):
            for j in range(width):
                r, g, b = 0, 0, 0
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        r += self.im[iSafe, jSafe][0] * mask[iOff + 1, jOff + 1]
                        g += self.im[iSafe, jSafe][1] * mask[iOff + 1, jOff + 1]
                        b += self.im[iSafe, jSafe][2] * mask[iOff + 1, jOff + 1]
                r, g, b = (abs(r)/2, abs(g)/2, abs(b)/2)
                if r > 255:
                    r = 255
                if g > 255:
                    g = 255
                if b > 255:
                    b = 255
                resultImage[i, j] = (r, g, b)

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "highpassPrewitt")

    # punkt 2, highpass 2
    def prewittGray(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        mask = np.zeros((3, 3))                               # [-1, 0, 1]
        mask[0, 0] = mask[1, 0] = mask[2, 0] = -1             # [-1, 0, 1]
        mask[0, 2] = mask[1, 2] = mask[2, 2] = 1              # [-1, 0, 1]

        # filtracja
        for i in range(height):
            for j in range(width):
                value = 0
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        value += self.im[iSafe, jSafe] * mask[iOff + 1, jOff + 1]
                resultImage[i, j] = abs(value / 2)

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.save(resultImage, self.imName, "highpassPrewitt")

    # punkt 2, highpass 3
    def sobolColor(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)
        tmp = np.empty((height, width, 3))
        tmp2 = np.empty((height, width, 3))

        mask = np.zeros((3, 3))                  # [1, 2, 1]
        mask[0, 0] = mask[0, 2] = 1              # [0, 0, 0]
        mask[2, 0] = mask[2, 2] = -1             # [-1,-2,-1]
        mask[0, 1] = 2
        mask[2, 1] = -2

        # filtracja
        for i in range(height):
            for j in range(width):
                r, g, b = 0, 0, 0
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        r += self.im[iSafe, jSafe][0] * mask[iOff + 1, jOff + 1]
                        g += self.im[iSafe, jSafe][1] * mask[iOff + 1, jOff + 1]
                        b += self.im[iSafe, jSafe][2] * mask[iOff + 1, jOff + 1]
                r = abs(r) / 2
                g = abs(g) / 2
                b = abs(b) / 2
                if r > 255:
                    r = 255
                if g > 255:
                    g = 255
                if b > 255:
                    b = 255
                resultImage[i, j] = (r, g, b)

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "highpassSobol")

    # punkt 2, highpass 3
    def sobolGray(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        mask = np.zeros((3, 3))                  # [1, 2, 1]
        mask[0, 0] = mask[0, 2] = 1              # [0, 0, 0]
        mask[2, 0] = mask[2, 2] = -1             # [-1,-2,-1]
        mask[0, 1] = 2
        mask[2, 1] = -2

        # filtracja
        for i in range(height):
            for j in range(width):
                value = 0
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        value += self.im[iSafe, jSafe] * mask[iOff + 1, jOff + 1]
                resultImage[i, j] = abs(value / 4)

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.save(resultImage, self.imName, "highpassSobol")

    #punkt 3, gradient 1
    def compassGray(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        mask = [0] * 8

        mask[0] = np.zeros((3, 3))        # [-1, 0, 1]
        mask[0][0, 2] = mask[0][2, 2] = 1   # [-2, 0, 2]
        mask[0][0, 0] = mask[0][2, 0] = -1  # [-1, 0, 1]
        mask[0][1, 2] = 2
        mask[0][1, 0] = -2

        mask[1] = np.zeros((3, 3))        # [0, 1, 2]
        mask[1][0, 1] = mask[1][1, 2] = 1   # [-1, 0, 1]
        mask[1][1, 0] = mask[1][2, 1] = -1  # [-2,-1,0]
        mask[1][0, 2] = 2
        mask[1][2, 0] = -2

        mask[2] = np.zeros((3, 3))        # [1, 2, 1]
        mask[2][0, 0] = mask[2][0, 2] = 1   # [0, 0, 0]
        mask[2][2, 0] = mask[2][2, 2] = -1  # [-1,-2,-1]
        mask[2][0, 1] = 2
        mask[2][2, 1] = -2

        mask[3] = np.zeros((3, 3))        # [2, 1, 0]
        mask[3][0, 1] = mask[3][1, 0] = 1   # [1, 0, -1]
        mask[3][1, 2] = mask[3][2, 1] = -1  # [0,-1,-2]
        mask[3][0, 0] = 2
        mask[3][2, 2] = -2

        mask[4] = np.zeros((3, 3))        # [1, 0, -1]
        mask[4][0, 0] = mask[4][2, 0] = 1   # [2, 0,-2]
        mask[4][0, 2] = mask[4][2, 2] = -1  # [1,0,-1]
        mask[4][1, 0] = 2
        mask[4][1, 2] = -2

        mask[5] = np.zeros((3, 3))        # [0, -1,-2]
        mask[5][1, 0] = mask[5][2, 1] = 1   # [1, 0, -1]
        mask[5][0, 1] = mask[5][1, 2] = -1  # [2, 1, 0]
        mask[5][2, 0] = 2
        mask[5][0, 2] = -2

        mask[6] = np.zeros((3, 3))        # [-1,-2,-1]
        mask[6][2, 0] = mask[6][2, 2] = 1   # [0, 0, 0]
        mask[6][0, 0] = mask[6][0, 2] = -1  # [1, 2, 1]
        mask[6][2, 1] = 2
        mask[6][0, 1] = -2

        mask[7] = np.zeros((3, 3))        # [-2,-1, 0]
        mask[7][1, 2] = mask[7][2, 1] = 1   # [-1, 0, 1]
        mask[7][0, 1] = mask[7][1, 0] = -1  # [ 0, 1, 2]
        mask[7][2, 2] = 2
        mask[7][0, 0] = -2

        # filtracja
        for i in range(height):
            for j in range(width):
                value = [0] * 8
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        for k in range(8):
                            value[k] += self.im[iSafe, jSafe] * mask[k][iOff + 1, jOff + 1]

                resultImage[i, j] = max(map(abs, value)) / 4

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.save(resultImage, self.imName, "compassSobol")

    #punkt 3, gradient 1
    def compassColor(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)
        tmp = np.empty((height, width, 3))
        tmp2 = np.empty((height, width, 3))

        mask = [0] * 8

        mask[0] = np.zeros((3, 3))        # [-1, 0, 1]
        mask[0][0, 2] = mask[0][2, 2] = 1   # [-2, 0, 2]
        mask[0][0, 0] = mask[0][2, 0] = -1  # [-1, 0, 1]
        mask[0][1, 2] = 2
        mask[0][1, 0] = -2

        mask[1] = np.zeros((3, 3))        # [0, 1, 2]
        mask[1][0, 1] = mask[1][1, 2] = 1   # [-1, 0, 1]
        mask[1][1, 0] = mask[1][2, 1] = -1  # [-2,-1,0]
        mask[1][0, 2] = 2
        mask[1][2, 0] = -2

        mask[2] = np.zeros((3, 3))        # [1, 2, 1]
        mask[2][0, 0] = mask[2][0, 2] = 1   # [0, 0, 0]
        mask[2][2, 0] = mask[2][2, 2] = -1  # [-1,-2,-1]
        mask[2][0, 1] = 2
        mask[2][2, 1] = -2

        mask[3] = np.zeros((3, 3))        # [2, 1, 0]
        mask[3][0, 1] = mask[3][1, 0] = 1   # [1, 0, -1]
        mask[3][1, 2] = mask[3][2, 1] = -1  # [0,-1,-2]
        mask[3][0, 0] = 2
        mask[3][2, 2] = -2

        mask[4] = np.zeros((3, 3))        # [1, 0, -1]
        mask[4][0, 0] = mask[4][2, 0] = 1   # [2, 0,-2]
        mask[4][0, 2] = mask[4][2, 2] = -1  # [1,0,-1]
        mask[4][1, 0] = 2
        mask[4][1, 2] = -2

        mask[5] = np.zeros((3, 3))        # [0, -1,-2]
        mask[5][1, 0] = mask[5][2, 1] = 1   # [1, 0, -1]
        mask[5][0, 1] = mask[5][1, 2] = -1  # [2, 1, 0]
        mask[5][2, 0] = 2
        mask[5][0, 2] = -2

        mask[6] = np.zeros((3, 3))        # [-1,-2,-1]
        mask[6][2, 0] = mask[6][2, 2] = 1   # [0, 0, 0]
        mask[6][0, 0] = mask[6][0, 2] = -1  # [1, 2, 1]
        mask[6][2, 1] = 2
        mask[6][0, 1] = -2

        mask[7] = np.zeros((3, 3))        # [-2,-1, 0]
        mask[7][1, 2] = mask[7][2, 1] = 1   # [-1, 0, 1]
        mask[7][0, 1] = mask[7][1, 0] = -1  # [ 0, 1, 2]
        mask[7][2, 2] = 2
        mask[7][0, 0] = -2

        # filtracja
        for i in range(height):
            for j in range(width):
                r = [0] * 8
                g = [0] * 8
                b = [0] * 8
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        for k in range(8):
                            r[k] += self.im[iSafe, jSafe][0] * mask[k][iOff + 1, jOff + 1]
                            g[k] += self.im[iSafe, jSafe][1] * mask[k][iOff + 1, jOff + 1]
                            b[k] += self.im[iSafe, jSafe][2] * mask[k][iOff + 1, jOff + 1]

                resultImage[i, j] = (max(map(abs, r)) / 4, max(map(abs, g)) / 4, max(map(abs, b)) / 4)

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "compassSobol")

    # punkt 3, gradient 2
    def reliefGray(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

#        mask = np.zeros((3, 3))     # [0, 0, 0]
#        mask[2, 1] = 1              # [0, 0,-1]
#        mask[1, 2] = -1             # [0, 1, 0]
#        mask[1, 1] = 1

        mask = np.zeros((3, 3))                               # [-1, 0, 1]
        mask[0, 0] = mask[1, 0] = mask[2, 0] = -1             # [-1, 0, 1]
        mask[0, 2] = mask[1, 2] = mask[2, 2] = 1              # [-1, 0, 1]
        mask[1, 1] = 1

        # filtracja
        for i in range(height):
            for j in range(width):
                value = 0
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        value += self.im[iSafe, jSafe] * mask[iOff + 1, jOff + 1]
                value = abs(value) / 2
                if value > 255:
                    value = 255
                resultImage[i, j] = value


        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.save(resultImage, self.imName, "reliefPrewitt")

    # punkt 3, gradient 2
    def reliefColor(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)
        tmp = np.empty((height, width, 3))
        tmp2 = np.empty((height, width, 3))

        mask = np.zeros((3, 3))                               # [-1, 0, 1]
        mask[0, 0] = mask[1, 0] = mask[2, 0] = -1             # [-1, 1, 1]
        mask[0, 2] = mask[1, 2] = mask[2, 2] = 1              # [-1, 0, 1]
        mask[1, 1] = 1

        # filtracja
        for i in range(height):
            for j in range(width):
                r, g, b = 0, 0, 0
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        r += self.im[iSafe, jSafe][0] * mask[iOff + 1, jOff + 1]
                        g += self.im[iSafe, jSafe][1] * mask[iOff + 1, jOff + 1]
                        b += self.im[iSafe, jSafe][2] * mask[iOff + 1, jOff + 1]
                r = abs(r) / 2
                g = abs(g) / 2
                b = abs(b) / 2
                if r > 255:
                    r = 255
                if g > 255:
                    g = 255
                if b > 255:
                    b = 255
                resultImage[i, j] = (r, g, b)

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "reliefPrewitt")

    # punkt 3, gradient 3
    def VDGGray(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        mask = [0] * 4

        mask[0] = np.zeros((3, 3))        # [-1, 0, 1]
        mask[0][0, 2] = mask[0][2, 2] = 1   # [-2, 0, 2]
        mask[0][0, 0] = mask[0][2, 0] = -1  # [-1, 0, 1]
        mask[0][1, 2] = 1
        mask[0][1, 0] = -1

        mask[1] = np.zeros((3, 3))        # [1, 2, 1]
        mask[1][0, 0] = mask[1][0, 2] = 1   # [0, 0, 0]
        mask[1][2, 0] = mask[1][2, 2] = -1  # [-1,-2,-1]
        mask[1][0, 1] = 1
        mask[1][2, 1] = -1

        mask[2] = np.zeros((3, 3))        # [1, 0, -1]
        mask[2][0, 0] = mask[2][2, 0] = 1   # [2, 0,-2]
        mask[2][0, 2] = mask[2][2, 2] = -1  # [1,0,-1]
        mask[2][1, 0] = 1
        mask[2][1, 2] = -1

        mask[3] = np.zeros((3, 3))        # [-1,-2,-1]
        mask[3][2, 0] = mask[3][2, 2] = 1   # [0, 0, 0]
        mask[3][0, 0] = mask[3][0, 2] = -1  # [1, 2, 1]
        mask[3][2, 1] = 1
        mask[3][0, 1] = -1

        # filtracja
        for i in range(height):
            for j in range(width):
                value = [0] * 4
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        for k in range(4):
                            value[k] += self.im[iSafe, jSafe] * mask[k][iOff + 1, jOff + 1]

                resultImage[i, j] = max(map(abs, value)) / 2

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.save(resultImage, self.imName, "vdgSobol")

    # punkt 3, gradient 3
    def VDGColor(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)
        tmp = np.empty((height, width, 3))
        tmp2 = np.empty((height, width, 3))

        mask = [0] * 4

        mask[0] = np.zeros((3, 3))        # [-1, 0, 1]
        mask[0][0, 2] = mask[0][2, 2] = 1   # [-2, 0, 2]
        mask[0][0, 0] = mask[0][2, 0] = -1  # [-1, 0, 1]
        mask[0][1, 2] = 1
        mask[0][1, 0] = -1

        mask[1] = np.zeros((3, 3))        # [1, 2, 1]
        mask[1][0, 0] = mask[1][0, 2] = 1   # [0, 0, 0]
        mask[1][2, 0] = mask[1][2, 2] = -1  # [-1,-2,-1]
        mask[1][0, 1] = 1
        mask[1][2, 1] = -1

        mask[2] = np.zeros((3, 3))        # [1, 0, -1]
        mask[2][0, 0] = mask[2][2, 0] = 1   # [2, 0,-2]
        mask[2][0, 2] = mask[2][2, 2] = -1  # [1,0,-1]
        mask[2][1, 0] = 1
        mask[2][1, 2] = -1

        mask[3] = np.zeros((3, 3))        # [-1,-2,-1]
        mask[3][2, 0] = mask[3][2, 2] = 1   # [0, 0, 0]
        mask[3][0, 0] = mask[3][0, 2] = -1  # [1, 2, 1]
        mask[3][2, 1] = 1
        mask[3][0, 1] = -1

        # filtracja
        for i in range(height):
            for j in range(width):
                r = [0] * 4
                g = [0] * 4
                b = [0] * 4
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        for k in range(4):
                            r[k] += self.im[iSafe, jSafe][0] * mask[k][iOff + 1, jOff + 1]
                            g[k] += self.im[iSafe, jSafe][1] * mask[k][iOff + 1, jOff + 1]
                            b[k] += self.im[iSafe, jSafe][2] * mask[k][iOff + 1, jOff + 1]

                resultImage[i, j] = (max(map(abs, r)) / 4, max(map(abs, g)) / 4, max(map(abs, b)) / 4)


        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "vdgSobol")

    # punkt 4, medianowy
    def medianGray(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                median = [0] * 9
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        median[3*(1 + iOff) + jOff + 1] = self.im[iSafe, jSafe]
                median.sort()
                u = int(round(len(median)/2))
                resultImage[i, j] = median[u] if ((u*2) % 2 == 0) else ((median[u - 1] + median[u])/2)

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.save(resultImage, self.imName, "median")

    # punkt 4, medianowy
    def medianColor(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                r = [0] * 9
                g = [0] * 9
                b = [0] * 9
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        r[3 * (1 + iOff) + jOff + 1] = self.im[iSafe, jSafe][0]
                        g[3 * (1 + iOff) + jOff + 1] = self.im[iSafe, jSafe][1]
                        b[3 * (1 + iOff) + jOff + 1] = self.im[iSafe, jSafe][2]
                r.sort()
                g.sort()
                b.sort()
                ur = int(round(len(r) / 2))
                ug = int(round(len(g) / 2))
                ub = int(round(len(b) / 2))
                resultImage[i, j] = (r[ur] if ((ur*2) % 2 == 0) else ((r[ur - 1] + r[ur])/2), g[ug] if ((ug*2) % 2 == 0) else ((g[ug - 1] + g[ug])/2), b[ub] if ((ub*2) % 2 == 0) else ((b[ub - 1] + b[ub])/2))

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "median")

    # punkt 5, maksymalny
    def maxGray(self, show=False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                median = [0] * 9
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        median[3 * (1 + iOff) + jOff + 1] = self.im[iSafe, jSafe]
                median.sort()
                resultImage[i, j] = median[len(median) - 1]

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.save(resultImage, self.imName, "max")

    # punkt 5, maksymalny
    def maxColor(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                r = [0] * 9
                g = [0] * 9
                b = [0] * 9
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        r[3 * (1 + iOff) + jOff + 1] = self.im[iSafe, jSafe][0]
                        g[3 * (1 + iOff) + jOff + 1] = self.im[iSafe, jSafe][1]
                        b[3 * (1 + iOff) + jOff + 1] = self.im[iSafe, jSafe][2]
                r.sort()
                g.sort()
                b.sort()
                resultImage[i, j] = (r[len(r) - 1], g[len(g) - 1], b[len(b) - 1])

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "max")

    # punkt 5, minimalny
    def minGray(self, show=False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                median = [0] * 9
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        median[3 * (1 + iOff) + jOff + 1] = self.im[iSafe, jSafe]
                median.sort()
                resultImage[i, j] = median[0]

        if show:
            self.show(Image.fromarray(resultImage, "L"))
        self.save(resultImage, self.imName, "min")

    # punkt 5, minimalny
    def minColor(self, show = False):
        width = self.im.shape[1]  # szereokść
        height = self.im.shape[0]  # wysokość

        # alokacja pamięci na obraz wynikowy
        resultImage = np.empty((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                r = [0] * 9
                g = [0] * 9
                b = [0] * 9
                for iOff in range(-1, 2):
                    for jOff in range(-1, 2):
                        iSafe = i if ((i + iOff) > (height - 1)) else (i + iOff)
                        jSafe = j if ((j + jOff) > (width - 1)) else (j + jOff)
                        r[3 * (1 + iOff) + jOff + 1] = self.im[iSafe, jSafe][0]
                        g[3 * (1 + iOff) + jOff + 1] = self.im[iSafe, jSafe][1]
                        b[3 * (1 + iOff) + jOff + 1] = self.im[iSafe, jSafe][2]
                r.sort()
                g.sort()
                b.sort()
                resultImage[i, j] = (r[0], g[0], b[0])

        if show:
            self.show(Image.fromarray(resultImage, "RGB"))
        self.save(resultImage, self.imName, "min")






    # metody użytkowe

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
        fileName = "img/zad9/"+ name + "_" + task + "_result.tiff"
        Image.fromarray(image).save(fileName)
        fileName = "img/zad9/"+ name + "_" + task + "_result.png"
        Image.fromarray(image).save(fileName)
