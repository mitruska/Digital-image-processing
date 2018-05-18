from PIL import Image
import numpy as np
import math


class ArithmeticColor:
        def __init__(self, image1Path = None, image2Path = None):
                if image1Path is not None:
                        # self.im1Name = self.getName(image1Path)
                        self.im1 = np.array(Image.open(image1Path))
                if image2Path is not None:
                        # self.im2Name = self.getName(image2Path)
                        self.im2 = np.array(Image.open(image2Path))

        # Sumowanie okreslonej stalej z obrazem
        def sum_const(self, const = 0, show = False, save = False):
            
                image_matrix = self.im1
                height = image_matrix.shape[0]   # wysokosc
                width = image_matrix.shape[1]    # szereoksc

                result_matrix = np.empty((height, width, 3), dtype=np.uint8)

                for y in range(height):
                        for x in range(width):  

                            # Obliczanie sum
                            R = int(image1_matrix[x][y][0]) + int(const)
                            G = int(image1_matrix[x][y][1]) + int(const)
                            B = int(image1_matrix[x][y][2]) + int(const)

                            # Szukanie maksymalnej wartosci
                            Q_max = max([R, G, B])
                            D_max = 0
                            X = 0

                            # Sprawdzenie czy maximum przekracza zakres
                            if Q_max > 255:
                                D_max = Q_max - 255
                                X = (D_max/255) # Obliczenie proporcji
                            
                            # Obliczenie sum z uwzglednieniem zakresu
                            R = (image1_matrix[x][y][0] - (image1_matrix[x][y][0] * X)) + (const - (const * X))
                            G = (image1_matrix[x][y][1] - (image1_matrix[x][y][1] * X)) + (const - (const * X))
                            B = (image1_matrix[x][y][2] - (image1_matrix[x][y][2] * X)) + (const - (const * X))

                            # Przypisanie nowych wartosci
                            result_matrix[x][y][0] = R
                            result_matrix[x][y][1] = G
                            result_matrix[x][y][2] = B

                if show == True:
                        #przed sumowaniem
                        Image.fromarray(image_matrix, "RGB").show()  
                        #po sumowaniu   
                        Image.fromarray(result_matrix, "RGB").show() 
                if save == True:
                        Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Const_Sum_Result.tiff", "TIFF")  


        def sum_img(self, show = False, save = False):
            
            image1_matrix = self.im1
            image2_matrix = self.im2
            height = image1_matrix.shape[0]   # wysokosc
            width = image1_matrix.shape[1]    # szereoksc

            result_matrix = np.empty((height, width, 3), dtype=np.uint8)

            for y in range(height):
                    for x in range(width):  

                            # Obliczanie sum
                            R = int(image1_matrix[x][y][0]) + int(image2_matrix[x][y][0])
                            G = int(image1_matrix[x][y][1]) + int(image2_matrix[x][y][1])
                            B = int(image1_matrix[x][y][2]) + int(image2_matrix[x][y][2])

                            # Szukanie maksymalnej wartosci
                            Q_max = max([R, G, B])
                            D_max = 0
                            X = 0

                            # Sprawdzenie czy maximum przekracza zakres
                            if Q_max > 255:
                                D_max = Q_max - 255
                                X = (D_max/255) # Obliczenie proporcji
                            
                            # Obliczenie sum z uwzglednieniem zakresu
                            R = (image1_matrix[x][y][0] - (image1_matrix[x][y][0] * X)) + (image2_matrix[x][y][0] - (image2_matrix[x][y][0] * X))
                            G = (image1_matrix[x][y][1] - (image1_matrix[x][y][1] * X)) + (image2_matrix[x][y][1] - (image2_matrix[x][y][1] * X))
                            B = (image1_matrix[x][y][2] - (image1_matrix[x][y][2] * X)) + (image2_matrix[x][y][2] - (image2_matrix[x][y][2] * X))

                            # Przypisanie nowych wartosci
                            result_matrix[x][y][0] = R
                            result_matrix[x][y][1] = G
                            result_matrix[x][y][2] = B


            if show == True:
                    #przed sumowaniem
                    Image.fromarray(image1_matrix, "RGB").show()  
                    Image.fromarray(image2_matrix, "RGB").show()  
                    #po sumowaniu   
                    Image.fromarray(result_matrix, "RGB").show() 
            if save == True:
                    Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Const_Sum_Result.tiff", "TIFF")  

        def multiply_const(self, const = 0, show = False, save = False):
            
            image_matrix = self.im1
            height = image_matrix.shape[0]   # wysokosc
            width = image_matrix.shape[1]    # szereoksc

            result_matrix = np.empty((height, width, 3), dtype=np.uint8)

            for y in range(height):
                for x in range(width):  

                    R = int(image_matrix[x][y][0])
                    G = int(image_matrix[x][y][1])
                    B = int(image_matrix[x][y][2])

                    if R == 255:
                        R = const
                    elif R == 0:
                        R = 0
                    else:
                        R = (int(image_matrix[x][y][0]) * int(const))/255 
                    
                    if G == 255:
                        G = const
                    elif G == 0:
                        G = 0
                    else:
                        G = (int(image_matrix[x][y][1]) * int(const))/255 
                    
                    if B == 255:
                        B = const
                    elif B == 0:
                        B = 0
                    else:
                        B = (int(image_matrix[x][y][2]) * int(const))/255 

                    # Przypisanie nowych wartosci
                    result_matrix[x][y][0] = R
                    result_matrix[x][y][1] = G
                    result_matrix[x][y][2] = B

            if show == True:
                    #przed sumowaniem
                    Image.fromarray(image_matrix, "RGB").show()  
                    #po sumowaniu   
                    Image.fromarray(result_matrix, "RGB").show() 
            if save == True:
                    Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Const_Sum_Result.tiff", "TIFF")  

        
        def multiply_img(self, show = False, save = False):

            image1_matrix = self.im1
            image2_matrix = self.im2
            height = image1_matrix.shape[0]   # wysokosc
            width = image1_matrix.shape[1]    # szereoksc

            result_matrix = np.empty((height, width, 3), dtype=np.uint8)

            for y in range(height):
                for x in range(width):  

                    R = int(image1_matrix[x][y][0])
                    G = int(image1_matrix[x][y][1])
                    B = int(image1_matrix[x][y][2])

                    if R == 255:
                        R = image2_matrix[x][y][0]
                    elif R == 0:
                        R = 0
                    else:
                        R = (int(image1_matrix[x][y][0]) * int(image2_matrix[x][y][0]))/255 
                    
                    if G == 255:
                        G = image2_matrix[x][y][1]
                    elif G == 0:
                        G = 0
                    else:
                        G = (int(image1_matrix[x][y][1]) * int(image2_matrix[x][y][1]))/255 
                    
                    if B == 255:
                        B = image2_matrix[x][y][2]
                    elif B == 0:
                        B = 0
                    else:
                        B = (int(image1_matrix[x][y][2]) * int(image2_matrix[x][y][2]))/255 

                    # Przypisanie nowych wartosci
                    result_matrix[x][y][0] = R
                    result_matrix[x][y][1] = G
                    result_matrix[x][y][2] = B

            if show == True:
                    #przed sumowaniem
                    Image.fromarray(image1_matrix, "RGB").show()  
                    Image.fromarray(image2_matrix, "RGB").show()  
                    #po sumowaniu   
                    Image.fromarray(result_matrix, "RGB").show() 
            if save == True:
                    Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Const_Sum_Result.tiff", "TIFF")  

        def mix_alfa(self, alfa = 1.0, show = False, save = False):
            
            image1_matrix = self.im1
            image2_matrix = self.im2
            height = image1_matrix.shape[0]   # wysokosc
            width = image1_matrix.shape[1]    # szereoksc

            result_matrix = np.empty((height, width, 3), dtype=np.uint8)

            for y in range(height):
                for x in range(width):  

                    # R = int(image1_matrix[x][y][0])
                    # G = int(image1_matrix[x][y][1])
                    # B = int(image1_matrix[x][y][2])

                    R = float(image1_matrix[x][y][0]) * alfa + (1-alfa) * float(image2_matrix[x][y][0])
                    G = float(image1_matrix[x][y][1]) * alfa + (1-alfa) * float(image2_matrix[x][y][1])
                    B = float(image1_matrix[x][y][2]) * alfa + (1-alfa) * float(image2_matrix[x][y][2])

                    # Przypisanie nowych wartosci
                    result_matrix[x][y][0] = math.ceil(R)
                    result_matrix[x][y][1] = math.ceil(G)
                    result_matrix[x][y][2] = math.ceil(B)
            
            
            if show == True:
                    #przed
                    Image.fromarray(image1_matrix, "RGB").show()  
                    Image.fromarray(image2_matrix, "RGB").show()  
                    #po    
                    Image.fromarray(result_matrix, "RGB").show() 
            if save == True:
                    Image.fromarray(result_matrix, "RGB").save("../../Resources/Color/Color_Const_Sum_Result.tiff", "TIFF")  



#TESTY
zad3 = ArithmeticColor(image1Path = "../../Resources/Color/Warzywa.tiff", image2Path = "../../Resources/Color/Szympans.tiff" )
# zad3.sum_const(const = 60, show = True, save = True)
# zad3.sum_img(show = True, save = True)
# zad3.multiply_img(show = True, save = True)
# zad3.multiply_const(const = 60, show = True, save = True)
zad3.mix_alfa(alfa = 0.3, show = True, save = True)
print(math.ceil(3.4))

