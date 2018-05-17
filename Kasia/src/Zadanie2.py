from PIL import Image
import numpy as np

# image_path = "../../Resources/Color/Kobieta.tiff"

# #SOME LIB TEST

# img = Image.open(image_path)
# img_wyjsciowy = Image.new("RGB", img.size)
# print(img.format)
# print(img.mode)
# print(img.size)
# print(img.width)
# print(img.height)

# pixels = list(img.getdata())
# print(pixels)

# print(img.getpixel((0,0)))
# R, G, B = img.getpixel((0,0))
# print("R={}, G={}, B={}".format(R, G, B))

#img.show()
def sum_const_color():
        image_path = "../../Resources/Color/Kobieta.tiff"
        img = Image.open(image_path)

        image_matrix = np.array(Image.open(image_path))
        rgb_matrix = np.empty((img.height, img.width, 3), dtype=np.uint8)
        Image.fromarray(rgb_matrix, "RGB").show()

        for y in range(img.height):
                for x in range(img.width):  
                        stala = 60 #stala

                        R = image_matrix[x][y][0]
                        G = image_matrix[x][y][1]
                        B = image_matrix[x][y][2]

                        R = R + const
                        G = G + const
                        B = B + const

                        if R > 255:
                                R = 255
                        if G > 255:
                                G = 255
                        if B > 255:
                                B = 255

                        #normalizacja
                        # maximum = 255
                        # if R > 255 or G > 255 or B > 255:
                        #         maximum = max([R, G, B])

                        # X = (maximum - 255) / 255
                        # R = stala - (stala * X) + image_matrix[x][y][0] - image_matrix[x][y][0] * X - 1
                        # G = stala - (stala * X) + image_matrix[x][y][1] - image_matrix[x][y][1] * X - 1
                        # B = stala - (stala * X) + image_matrix[x][y][2] - image_matrix[x][y][2] * X - 1

                        rgb_matrix[x][y][0] = R
                        rgb_matrix[x][y][1] = G
                        rgb_matrix[x][y][2] = B

        img.show()
        Image.fromarray(rgb_matrix, "RGB").show()


def sum_const_gray():
        # image_path = "../../Resources/Color/Kobieta.tiff"

        image_path = "../../Resources/Gray/Zegarek.tiff"
        img = Image.open(image_path)

        image_matrix = np.array(Image.open(image_path))
        print("Image shape", image_matrix.shape)
        gray_matrix = np.empty((img.height, img.width), dtype=np.uint8)
        Image.fromarray(gray_matrix, "L").show()

        for y in range(img.height):
                for x in range(img.width):  
                        const = 60 #stala

                        L = image_matrix[x][y]
                        L = L + const

                        maximum = 255
                        if L > 255:
                                maximum = L
                                L = 255

                        # X = (maximum - 255) / 255
                        # L = stala - (stala * X) + image_matrix[x][y] - image_matrix[x][y] * X - 1

                        gray_matrix[x][y] = L

        Image.fromarray(gray_matrix, "L").show()


# sum_const_gray()
# sum_const_color()


# #ZADANIE 2

class ArithmeticGray:
        def __init__(self, image1Path = None, image2Path = None):
                if image1Path is not None:
                        # self.im1Name = self.getName(image1Path)
                        self.im1 = np.array(Image.open(image1Path))
                if image2Path is not None:
                        # self.im2Name = self.getName(image2Path)
                        self.im2 = np.array(Image.open(image2Path))

        def sum_const(self, const = 0, show = False, save = False):
            # image_path = "../../Resources/Color/Kobieta.tiff"

                # image_path = "../../Resources/Gray/Zegarek.tiff"
                # img = Image.open(image_path)

                image_matrix = self.im1
                width = image_matrix.shape[1]    # szereokść
                height = image_matrix.shape[0]   # wysokość

                gray_matrix = np.empty((height, width), dtype=np.uint8)

                for y in range(height):
                        for x in range(width):  

                                L = image_matrix[x][y]
                                L = L + const

                                maximum = 255
                                if L > 255:
                                        maximum = L
                                        L = 255

                                gray_matrix[x][y] = L

                if show == True:
                        #przed sumowaniem
                        Image.fromarray(image_matrix, "L").show()  
                        #po sumowaniu   
                        Image.fromarray(gray_matrix, "L").show() 
                if save == True:
                        Image.fromarray(gray_matrix, "L").save("../../Resources/Gray/Gray_Const_Sum_Result.tiff", "TIFF")  





zad2 = ArithmeticGray(image1Path = "../../Resources/Gray/Zegarek.tiff")
zad2.sum_const_gray(const = 60, show = True, save = True)