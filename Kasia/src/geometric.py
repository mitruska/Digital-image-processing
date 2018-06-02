from PIL import Image
import numpy as np
import math

class Geometric:
    def __init__(self, image1Path = None, image2Path = None):
        if image1Path is not None:
                image = Image.open(image1Path)
                self.im1 = np.array(image)
        if image2Path is not None:
                # self.im2Name = self.getName(image2Path)
                self.im2 = np.array(Image.open(image2Path))

    def move(self, delta_x = 0, delta_y = 0, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc


        #PRZESUNIECIE BEZ UCIECIA
        # result_matrix = np.empty((height + delta_y, width + delta_y, 3), dtype=np.uint8)

        # for y in range(height):
        #     for x in range(width):  
        #         result_matrix[y+delta_y][x+delta_x] = image_matrix[y][x]


        #PRZECUNIECIE Z UCIECIEM
        result_matrix = np.empty((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):  
                if y+delta_y < height and x+delta_x < width:
                    result_matrix[y+delta_y][x+delta_x] = image_matrix[y][x]
        
        if show == True:
            #przed 
            Image.fromarray(image_matrix).show()  
            #po    
            Image.fromarray(result_matrix).show() 
        if save == True:
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Move_Result.tiff", "TIFF")  

    def scale(self, scale_x = 1, scale_y = 1, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        # result_matrix = np.empty((math.ceil(height/scale_y), math.ceil(width/scale_x), 3), dtype=np.uint8)
        result_matrix = np.empty((height, width, 3), dtype=np.uint8)

        # scale_height = 0
        # scale_width = 0

        for y in range(height):
            for x in range(width): 
                if scale_y*y < height and scale_x*x < width:
                    # result_matrix[y][x] = image_matrix[scale_y*y][scale_x*x]
                    result_matrix[int(scale_y*y)][int(scale_x*x)] = image_matrix[y][x]
        
        if show == True:
            #przed 
            Image.fromarray(image_matrix).show()  
            #po    
            Image.fromarray(result_matrix).show() 
        if save == True:
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Scale_Result.tiff", "TIFF")  


geo = Geometric(image1Path = "../../Resources/Color/Warzywa.tiff", image2Path = "../../Resources/Color/Szympans.tiff" )
# geo.move(40, 60, True, True)
# geo.scale(5, 4, True, True)
geo.scale(0.2, 0.3, True, True)