from PIL import Image
from os import remove
import numpy as np


# ZADANIE 1
class Unification:
    def __init__(self, image1Path = None, image2Path = None):
        if image1Path is not None:
            self.im1Name = self.getName(image1Path)
            self.im1 = np.array(Image.open(image1Path))
        if image2Path is not None:
            self.im2Name = self.getName(image2Path)
            self.im2 = np.array(Image.open(image2Path))

    # punkt 1
    def geometricGray(self, show = False):
        # największa szerokość spośród dwuch obrazów
        width1 = self.im1.shape[1]
        width2 = self.im2.shape[1]
        maxWidth = width1 if width1 > width2 else width2

        # największa wysokość spośród dwuch obrazów
        height1 = self.im1.shape[0]
        height2 = self.im2.shape[0]
        maxHeight = height1 if height1 > height2 else height2

        # alokacja pamięci na obrazy wynikowe
        resultImage1 = np.empty((maxHeight, maxWidth), dtype = np.uint8)
        resultImage2 = np.empty((maxHeight, maxWidth), dtype = np.uint8)

        # współrzędne początku rysowania obrazu 1 w środku
        startWidthCoord = int(round((maxWidth - width1) / 2))
        startHeightCoord = int(round((maxHeight - height1) / 2))

        # wypełnienie obrazu czarny kolorem
        for i in range(0, maxHeight):
            for j in range(0, maxWidth):
                resultImage1[i, j] = 1

        # narysowanie wyśrodkowanego obrazu
        for i in range(0, height1):
            for j in range(0, width1):
                resultImage1[i + startHeightCoord, j + startWidthCoord] = self.im1[i, j]

        # współrzędne początku rysowania obrazu 1 w środku
        startWidthCoord = int(round((maxWidth - width2) / 2))
        startHeightCoord = int(round((maxHeight - height2) / 2))

        # wypełnienie obrazu czarnym kolorem
        for i in range(0, maxHeight):
            for j in range(0, maxWidth):
                resultImage2[i, j] = 1

        # narysowanie wyśrodkowanego obrazu
        for i in range(0, height2):
            for j in range(0, width2):
                resultImage2[i + startHeightCoord, j + startWidthCoord] = self.im2[i, j]

        if show:
            self.show(Image.fromarray(resultImage1, "L"), Image.fromarray(resultImage2, "L"))
        self.save(resultImage1, self.im1Name, "unificationGeo")
        self.save(resultImage2, self.im2Name, "unificationGeo")

    # punkt 3
    def geometricColor(self, show = False):
        # największa szerokość spośród dwuch obrazów
        width1 = self.im1.shape[1]
        width2 = self.im2.shape[1]
        maxWidth = width1 if width1 > width2 else width2

        # największa wysokość spośród dwuch obrazów
        height1 = self.im1.shape[0]
        height2 = self.im2.shape[0]
        maxHeight = height1 if height1 > height2 else height2

        # alokacja pamięci na obrazy wynikowe
        resultImage1 = np.empty((maxHeight, maxWidth, 3), dtype = np.uint8)
        resultImage2 = np.empty((maxHeight, maxWidth, 3), dtype = np.uint8)

        # współrzędne początku rysowania obrazu 1 w środku
        startWidthCoord = int(round((maxWidth - width1) / 2))
        startHeightCoord = int(round((maxHeight - height1) / 2))

        # wypełnienie obrazu biały kolorem
        for i in range(0, maxHeight):
            for j in range(0, maxWidth):
                resultImage1[i, j] = (1, 1, 1)

        # narysowanie wyśrodkowanego obrazu
        for i in range(0, height1):
            for j in range(0, width1):
                resultImage1[i + startHeightCoord, j + startWidthCoord] = self.im1[i, j]

        # współrzędne początku rysowania obrazu 1 w środku
        startWidthCoord = int(round((maxWidth - width2) / 2))
        startHeightCoord = int(round((maxHeight - height2) / 2))

        # wypełnienie obrazu biały kolorem
        for i in range(0, maxHeight):
            for j in range(0, maxWidth):
                resultImage2[i, j] = (1, 1, 1)

        # narysowanie wyśrodkowanego obrazu
        for i in range(0, height2):
            for j in range(0, width2):
                resultImage2[i + startHeightCoord, j + startWidthCoord] = self.im2[i, j]

        if show:
            self.show(Image.fromarray(resultImage1, "RGB"), Image.fromarray(resultImage2, "RGB"))
        self.save(resultImage1, self.im1Name, "unificationGeo")
        self.save(resultImage2, self.im2Name, "unificationGeo")

    # punkt 2
    def rasterGray(self, show = False):
        # pierwszy jest ZAWSZE większy
        width1 = self.im1.shape[1]
        width2 = self.im2.shape[1]

        height1 = self.im1.shape[0]
        height2 = self.im2.shape[0]

        scaleW = width1 / width2
        scaleH = height1 / height2

        # alokacja pamięci na obrazy wynikowe
        resultImage1 = np.zeros((height1, width1), dtype = np.uint8)
        resultImage2 = np.zeros((height1, width1), dtype = np.uint8)
        tmp = np.zeros((height1, width1), dtype = np.uint8)

        for i in range(height1):
            for j in range(width1):
                resultImage1[i, j] = self.im1[i, j]

        # wypełnianie
        count = 0
        for i in range(height2):
            for j in range(width2):
                if count == 0:
                    resultImage2[int(scaleH*i), int(round(scaleW*j)) + 1] = self.im2[i, j]
                    count += 1
                if count == 1:
                    resultImage2[int(round(scaleH*i)) + 1, int(scaleW*j)] = self.im2[i, j]
                    count = 0

        # interpolacja
        for i in range(height1):
            for j in range(width1):
                value = 0
                n = 0
                tmp[i, j] = resultImage2[i, j]
                if resultImage2[i, j] < 1:
                    for iOff in range(-1, 2):
                        for jOff in range(-1, 2):
                            iSafe = i if ((i + iOff) > (height1 - 2)) | ((i + iOff) < 0) else (i + iOff)
                            jSafe = j if ((j + jOff) > (width1 - 2)) | ((j + jOff) < 0) else (j + jOff)
                            if resultImage2[iSafe, jSafe] > 0:
                                value += resultImage2[iSafe, jSafe]
                                n += 1
                    tmp[i, j] = value / n
                    resultImage2[i, j] = tmp[i, j]

        if show:
            self.show(Image.fromarray(resultImage1, "L"), Image.fromarray(resultImage2, "L"))
        self.save(resultImage1, self.im1Name, "unificationRas")
        self.save(resultImage2, self.im2Name, "unificationRas")

    # punkt 4
    def rasterColor(self, show = False):
        # pierwszy jest ZAWSZE większy
        width1 = self.im1.shape[1]
        width2 = self.im2.shape[1]

        height1 = self.im1.shape[0]
        height2 = self.im2.shape[0]

        scaleW = width1 / width2
        scaleH = height1 / height2

        # alokacja pamięci na obrazy wynikowe
        resultImage1 = np.zeros((height1, width1, 3), dtype = np.uint8)
        resultImage2 = np.zeros((height1, width1, 3), dtype = np.uint8)
        tmp = np.zeros((height1, width1, 3), dtype = np.uint8)

        for i in range(height1):
            for j in range(width1):
                resultImage1[i, j] = self.im1[i, j]

        # wypełnianie
        count = 0
        for i in range(height2):
            for j in range(width2):
                if count == 0:
                    resultImage2[int(scaleH*i), int(round(scaleW*j)) + 1] = self.im2[i, j]
                    count += 1
                if count == 1:
                    resultImage2[int(round(scaleH*i)) + 1, int(scaleW*j)] = self.im2[i, j]
                    count = 0

        # interpolacja
        for i in range(height1):
            for j in range(width1):
                r, g, b = 0, 0, 0
                n = 0
                tmp[i, j] = resultImage2[i, j]
                if (resultImage2[i, j][0] < 1) & (resultImage2[i, j][1] < 1) & (resultImage2[i, j][2] < 1):
                    for iOff in range(-1, 2):
                        for jOff in range(-1, 2):
                            iSafe = i if ((i + iOff) > (height1 - 2)) | ((i + iOff) < 0) else (i + iOff)
                            jSafe = j if ((j + jOff) > (width1 - 2)) | ((j + jOff) < 0) else (j + jOff)
                            if (resultImage2[iSafe, jSafe][0] > 0) | (resultImage2[iSafe, jSafe][1] > 0) | (resultImage2[iSafe, jSafe][2] > 0):
                                r += resultImage2[iSafe, jSafe][0]
                                g += resultImage2[iSafe, jSafe][1]
                                b += resultImage2[iSafe, jSafe][2]
                                n += 1
                    tmp[i, j] = (r/n, g/n, b/n)
                    resultImage2[i, j] = tmp[i, j]

        if show:
            self.show(Image.fromarray(resultImage1, "RGB"), Image.fromarray(resultImage2, "RGB"))
        self.save(resultImage1, self.im1Name, "unificationRas")
        self.save(resultImage2, self.im2Name, "unificationRas")





    def load(self, image1Path, image2Path):
        self.im1Name = self.getName(image1Path)
        self.im2Name = self.getName(image2Path)
        self.im1 = np.array(Image.open(image1Path))
        self.im2 = np.array(Image.open(image2Path))

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
        fileName = "img/zad1/"+ name + "_" + task + "_result.tiff"
        Image.fromarray(image).save(fileName)
        fileName = "img/zad1/" + name + "_" + task + "_result.png"
        Image.fromarray(image).save(fileName)



#def grayscale(self):
#    for i in range(0, self.height):
#        for j in range(0, self.width):
#            r, g, b = self.pix[i, j]
#            gray = int(round(0.21 * r + 0.71 * g + 0.07 * b / 3))
#            self.pix[i, j] = (gray, gray, gray)

