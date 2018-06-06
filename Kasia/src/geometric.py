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
        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)

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

    def scale_j(self, scale = 1, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        # result_matrix = np.empty((math.ceil(height/scale_y), math.ceil(width/scale_x), 3), dtype=np.uint8)
        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)

        # scale_height = 0
        # scale_width = 0

        for y in range(height):
            for x in range(width): 
                if scale*y < height and scale*x < width:
                    # result_matrix[y][x] = image_matrix[scale*y][scale*x]
                    result_matrix[int(scale*y)][int(scale*x)] = image_matrix[y][x]
        
        if show == True:
            #przed 
            Image.fromarray(image_matrix).show()  
            #po    
            Image.fromarray(result_matrix).show() 
        if save == True:
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Scale_Result.tiff", "TIFF")  


    def scale_nj(self, scale_x = 1, scale_y = 1, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        # result_matrix = np.empty((math.ceil(height/scale_y), math.ceil(width/scale_x), 3), dtype=np.uint8)
        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)

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


    def turn(self, alfa = 0, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        #przeksztalcenie na radiany
        alfa_r = math.radians(alfa)

        # result_matrix = np.empty((math.ceil(height/scale_y), math.ceil(width/scale_x), 3), dtype=np.uint8)
        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)
        # result_matrix.fill(255)

        for y in range(height):
            for x in range(width): 
                # new_x = x*math.cos(alfa_r) - y*math.sin(alfa_r)
                # new_y = x*math.sin(alfa_r) + y*math.cos(alfa_r)

                new_x = (x - width/2) * math.cos(alfa_r) - (y - height/2) * math.sin(alfa_r) + (width/2)
                new_y = (x - width/2) * math.sin(alfa_r) + (y - height/2) * math.cos(alfa_r) + (height/2)
                if new_y < height and new_y >= 0 and new_x >= 0 and new_x < width:
                    # result_matrix[y][x] = image_matrix[scale*y][scale*x]
                    result_matrix[int(new_y)][int(new_x)] = image_matrix[y][x]
                    # result_matrix[y][x] = image_matrix[int(new_y)][int(new_x)]
                else:
                    pass
                    

        resultImage2 = np.copy(result_matrix)
        tmp = np.ones((height, width, 3), dtype = np.uint8)

        for i in range(height):
            for j in range(width):
                r, g, b = 0, 0, 0
                n = 1
                tmp[i, j] = resultImage2[i, j]
                if (resultImage2[i, j][0] < 1) & (resultImage2[i, j][1] < 1) & (resultImage2[i, j][2] < 1):
                    for iOff in range(-1, 2):
                        for jOff in range(-1, 2):
                            iSafe = i if ((i + iOff) > (height - 2)) | ((i + iOff) < 0) else (i + iOff)
                            jSafe = j if ((j + jOff) > (width - 2)) | ((j + jOff) < 0) else (j + jOff)
                            if (resultImage2[iSafe, jSafe][0] > 0) | (resultImage2[iSafe, jSafe][1] > 0) | (resultImage2[iSafe, jSafe][2] > 0):
                                r += resultImage2[iSafe, jSafe][0]
                                g += resultImage2[iSafe, jSafe][1]
                                b += resultImage2[iSafe, jSafe][2]
                                n += 1
                    tmp[i, j] = (r/n, g/n, b/n)
                    resultImage2[i, j] = tmp[i, j]
        
        if show == True:
            #przed 
            Image.fromarray(image_matrix).show()  
            #po    
            Image.fromarray(result_matrix).show() 
            Image.fromarray(resultImage2).show() 

        if save == True:
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Scale_Result.tiff", "TIFF")  


    def sym_x(self, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)
        _height = height-1 #array height last index

        for y in range(height):
            for x in range(width): 
                    result_matrix[y][x] = image_matrix[_height-y][x]
        
        if show == True:
            #przed 
            Image.fromarray(image_matrix).show()  
            #po    
            Image.fromarray(result_matrix).show() 
        if save == True:
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Scale_Result.tiff", "TIFF")  

    def sym_y(self, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)
        _width = width - 1 #array width last index

        for y in range(height):
            for x in range(width): 
                    result_matrix[y][x] = image_matrix[y][_width - x]
        
        if show == True:
            #przed 
            Image.fromarray(image_matrix).show()  
            #po    
            Image.fromarray(result_matrix).show() 
        if save == True:
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Scale_Result.tiff", "TIFF")  

    def sym_paramy(self, param_y = 0, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)
        _height = height - 1 #array height last index
 
        param_y = height/2

        for y in range(height):
            for x in range(width): 
                if y < param_y:
                    result_matrix[y][x] = image_matrix[y][x]
                else:
                    result_matrix[y][x] = image_matrix[_height - y][x]

        if show == True:
            #przed 
            Image.fromarray(image_matrix).show()  
            #po    
            Image.fromarray(result_matrix).show() 
        if save == True:
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Scale_Result.tiff", "TIFF")  




    def sym_paramx(self, param_x = 0, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)
        _width = width - 1 #array width last index
 
        param_x = width/2

        for y in range(height):
            for x in range(width): 
                if x < param_x:
                    result_matrix[y][x] = image_matrix[y][x]
                else:
                    result_matrix[y][x] = image_matrix[y][_width - x]
        
        if show == True:
            #przed 
            Image.fromarray(image_matrix).show()  
            #po    
            Image.fromarray(result_matrix).show() 
        if save == True:
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Scale_Result.tiff", "TIFF")  

    def cut_frg(self, x_min, x_max, y_min, y_max, show = False, save = False):
        
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width): 
                #poruszamy się w pierwszej ćwiartce osi układu współrzędnych
                if x > x_min and x < x_max and y < height-y_min and y > height-y_max:
                    result_matrix[y][x] = 0
                else:
                    result_matrix[y][x] = image_matrix[y][x]
        
        if show == True:
            #przed 
            Image.fromarray(image_matrix).show()  
            #po    
            Image.fromarray(result_matrix).show() 
        if save == True:
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Scale_Result.tiff", "TIFF")  

    def copy_frg(self, x_min, x_max, y_min, y_max, show = False, save = False):
        
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)
        
        #macierz o wymiarach wycinanego fragmentu
        cut_matrix = np.zeros((y_max-y_min + 1, x_max-x_min + 1, 3), dtype=np.uint8)

        cut_y = 0
        for y in range(height):
            cut_x = 0
            for x in range(width): 
                #poruszamy się w pierwszej ćwiartce osi układu współrzędnych
                if x >= x_min and x <= x_max and y <= height-y_min and y >= height-y_max:    
                    result_matrix[y][x] = image_matrix[y][x]
                    cut_matrix[cut_y][cut_x] = image_matrix[y][x]
                    cut_x+=1
            if cut_x > 0:    
                cut_y+=1

        
        
        if show == True:
            #przed 
            Image.fromarray(image_matrix).show()  
            #po    
            Image.fromarray(result_matrix).show() 
            Image.fromarray(cut_matrix).show()  

        if save == True:
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Scale_Result.tiff", "TIFF")  



geo = Geometric(image1Path = "../../Resources/Color/Warzywa.tiff", image2Path = "../../Resources/Color/Szympans.tiff" )
# geo.move(40, 60, True, True)
# geo.scale(5, 4, True, True)
# geo.scale_j(5, True, True)
# geo.turn(20, True, True)
# geo.sym_x(True, True)
# geo.sym_paramx(True, True)
# geo.cut_frg(5,20,40,80, True, True)
geo.copy_frg(5,20,40,80, True, True)