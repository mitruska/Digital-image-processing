from PIL import Image
import numpy as np
import math

class Geometric:
    def __init__(self, im1Name_ = "1", image1Path = None, image2Path = None):
        if image1Path is not None:
                image = Image.open(image1Path)
                self.im1 = np.array(image)
                self.im1Name = im1Name_
        if image2Path is not None:
                # self.im2Name = self.getName(image2Path)
                self.im2 = np.array(Image.open(image2Path))

    def move(self, delta_x = 0, delta_y = 0, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        delta_y = 0 - delta_y # Poruszamy sie w pierwszej cwartce ukladu wspolrzednyvh

        #PRZESUNIECIE BEZ UCIECIA
        # result_matrix = np.empty((height + delta_y, width + delta_y, 3), dtype=np.uint8)

        # for y in range(height):
        #     for x in range(width):  
        #         result_matrix[y+delta_y][x+delta_x] = image_matrix[y][x]


        #PRZECUNIECIE Z UCIECIEM
        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):  
                if 0 < y+delta_y < height and 0 < x+delta_x < width:
                    result_matrix[y+delta_y][x+delta_x] = image_matrix[y][x]
        
        if show == True:
            #przed 
            Image.fromarray(image_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()

        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_Move_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_Move_Result.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_Move_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_Move_Result.png", "PNG")  


    def scale_j(self, scale = 1, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        # result_matrix = np.empty((math.ceil(height/scale_y), math.ceil(width/scale_x), 3), dtype=np.uint8)
        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width): 
                if scale*y < height and scale*x < width:
                    # result_matrix[y][x] = image_matrix[scale*y][scale*x]
                    result_matrix[int(scale*y)][int(scale*x)] = image_matrix[y][x]

        resultImage2 = np.copy(result_matrix)
        tmp = np.ones((height, width, 3), dtype = np.uint8)
        
        # Interpolacja
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
            Image.fromarray(image_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
            #po interpolacji
            Image.fromarray(resultImage2, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_ScaleJ_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_ScaleJ_Result.tiff", "TIFF")  
            Image.fromarray(resultImage2, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_ScaleJ_Result_Interp.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_ScaleJ_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_ScaleJ_Result.png", "PNG")  
            Image.fromarray(resultImage2, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_ScaleJ_Result_Interp.png", "PNG")  

    def scale_nj(self, scale_x = 1, scale_y = 1, show = False, save = False):
        
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        # result_matrix = np.empty((math.ceil(height/scale_y), math.ceil(width/scale_x), 3), dtype=np.uint8)
        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width): 
                if scale_y*y < height and scale_x*x < width:
                    # result_matrix[y][x] = image_matrix[scale_y*y][scale_x*x]
                    result_matrix[int(scale_y*y)][int(scale_x*x)] = image_matrix[y][x]
        
        resultImage2 = np.copy(result_matrix)
        tmp = np.ones((height, width, 3), dtype = np.uint8)

        # Interpolacja
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
            Image.fromarray(image_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
            #po interpolacji
            Image.fromarray(resultImage2, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_ScaleNJ_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_ScaleNJ_Result.tiff", "TIFF")  
            Image.fromarray(resultImage2, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_ScaleJN_Result_Interp.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_ScaleNJ_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_ScaleNJ_Result.png", "PNG")  
            Image.fromarray(resultImage2, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_ScaleNJ_Result_Interp.png", "PNG")  


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
                    

        resultImage2 = np.copy(result_matrix)
        tmp = np.ones((height, width, 3), dtype = np.uint8)

        # Interpolacja
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
            Image.fromarray(image_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
            #po interpolacji
            Image.fromarray(resultImage2, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_Turn_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_Turn_Result.tiff", "TIFF")  
            Image.fromarray(resultImage2, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_Turn_Result_Interp.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_Turn_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_Turn_Result.png", "PNG")  
            Image.fromarray(resultImage2, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_Turn_Result_Interp.png", "PNG")  

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
            Image.fromarray(image_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_ox_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_ox_Result.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_ox_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_ox_Result.png", "PNG")  

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
            Image.fromarray(image_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_oy_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_oy_Result.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_oy_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_oy_Result.png", "PNG")  

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
            Image.fromarray(image_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_py_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_py_Result.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_py_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_py_Result.png", "PNG")  



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
            Image.fromarray(image_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_px_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_px_Result.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_px_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_px_Result.png", "PNG")  

    def cut_frg(self, x_min, x_max, y_min, y_max, show = False, save = False):
        
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width): 
                # Poruszamy się w pierwszej cwiartce osi układu wspolrzednych
                if x > x_min and x < x_max and y < height-y_min and y > height-y_max:
                    result_matrix[y][x] = 0
                else:
                    result_matrix[y][x] = image_matrix[y][x]
        
        if show == True:
            #przed 
            Image.fromarray(image_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_Cut_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_Cut_Result.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_Cut_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_Cut_Result.png", "PNG")  

    def copy_frg(self, x_min, x_max, y_min, y_max, show = False, save = False):
        
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Macierz o wymiarach wycinanego fragmentu
        cut_matrix = np.zeros((y_max-y_min + 1, x_max-x_min + 1, 3), dtype=np.uint8)

        cut_y = 0
        for y in range(height):
            cut_x = 0
            for x in range(width): 
                # Poruszamy się w pierwszej cwiartce osi układu wspolrzednych
                if x >= x_min and x <= x_max and y <= height-y_min and y >= height-y_max:    
                    result_matrix[y][x] = image_matrix[y][x]
                    cut_matrix[cut_y][cut_x] = image_matrix[y][x]
                    cut_x+=1
            if cut_x > 0:    
                cut_y+=1

        if show == True:
            #przed 
            Image.fromarray(image_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
            #po wycieciu
            Image.fromarray(cut_matrix, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_Copy_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_Copy_Result.tiff", "TIFF")  
            Image.fromarray(cut_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Geo_Copy_Result_Interp.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_Copy_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_Copy_Result.png", "PNG")  
            Image.fromarray(cut_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Geo_Copy_Result_Interp.png", "PNG")  



# geo = Geometric(image1Path = "../../Resources/Color/Warzywa.tiff", image2Path = "../../Resources/Color/Szympans.tiff" )
# # geo.move(40, 70, True, True)
# # geo.scale_nj(2, 1, True, True)
# # geo.scale_j(1.5, True, True)
# # geo.turn(45, True, True)
# # geo.sym_x(True, True)
# # geo.sym_y(True, True)
# geo.sym_paramx(show = True, save = True)
# geo.sym_paramy(show = True, save = True)
# # geo.cut_frg(100,250,25,450, True, True)
# # geo.copy_frg(100,250,25,450, True, True)

# geo2 = Geometric(im1Name_='2', image1Path = "../../Resources/Color/Statek.tiff", image2Path = "../../Resources/Color/Szympans.tiff" )
# # geo2.move(200, 100, True, True)
# # geo2.scale_nj(1, 2, True, True)
# # geo2.scale_j(2, True, True)
# # geo2.turn(110, True, True)
# # geo2.sym_x(True, True)
# # geo2.sym_y(True, True)
# geo2.sym_paramx(show = True, save = True)
# geo2.sym_paramy(show = True, save = True)
# # geo2.cut_frg(200,400,200,400, True, True)
# # geo2.copy_frg(200,400,200,400, True, True)

