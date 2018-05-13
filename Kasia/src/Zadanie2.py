from PIL import Image
import numpy as np

image_path = "../../Resources/Color/Kobieta.tiff"

#SOME LIB TEST

img = Image.open(image_path)
print(img.format)
print(img.mode)
print(img.size)
print(img.width)
print(img.height)

# pixels = list(img.getdata())
# print(pixels)

print(img.getpixel((0,0)))
R, G, B = img.getpixel((0,0))
print("R={}, G={}, B={}".format(R, G, B))s

#img.show()

rgb_matrix = np.zeros((3, img.width, img.height))
print(rgb_matrix)

for y in range(img.height):
    for x in range(img.width):
        R, G, B = img.getpixel((x ,y))
        const_var = 40 #stala

        R = R + const_var
        G += const_var
        B += const_var

        rgb_matrix[0][x][y] = R
        rgb_matrix[1][x][y] = G
        rgb_matrix[2][x][y] = B


print(rgb_matrix)


        # if R>255 || G>255 || B>255:
        #     max_

