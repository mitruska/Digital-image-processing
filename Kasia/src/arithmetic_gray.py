from PIL import Image
import numpy as np


class ArithmeticGray:
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
                width = image_matrix.shape[1]    # szereoksc
                height = image_matrix.shape[0]   # wysokosc

                result_matrix = np.empty((height, width), dtype=np.uint8)

                for y in range(height):
                    for x in range(width):  

                            # Obliczanie sumy
                            L = int(image1_matrix[x][y]) + int(const)

                            Q_max = L
                            D_max = 0
                            X = 0

                            # Sprawdzenie czy przekracza zakres
                            if Q_max > 255:
                                D_max = Q_max - 255
                                X = (D_max/255)

                            # Obliczenie sumy z uwzglednieniem zakresu
                            L = (image1_matrix[x][y] - (image1_matrix[x][y] * X)) + (const - (const * X))

                            # Przypisanie nowej wartosci
                            result_matrix[x][y] = L

                if show == True:
                        #przed sumowaniem
                        Image.fromarray(image_matrix, "L").show()  
                        #po sumowaniu   
                        Image.fromarray(result_matrix, "L").show() 
                if save == True:
                        Image.fromarray(result_matrix, "L").save("../../Resources/Gray/Gray_Const_Sum_Result.tiff", "TIFF")  

        def sum_img(self, show = False, save = False):
            
            image1_matrix = self.im1
            image2_matrix = self.im2
            height = image1_matrix.shape[0]   # wysokosc
            width = image1_matrix.shape[1]    # szereoksc

            result_matrix = np.empty((height, width), dtype=np.uint8)

            for y in range(height):
                    for x in range(width):  

                            # Obliczanie sumy
                            L = int(image1_matrix[x][y]) + int(image2_matrix[x][y])

                            Q_max = L
                            D_max = 0
                            X = 0

                            # Sprawdzenie czy przekracza zakres
                            if Q_max > 255:
                                D_max = Q_max - 255
                                X = (D_max/255)

                            # Obliczenie sumy z uwzglednieniem zakresu
                            L = (image1_matrix[x][y] - (image1_matrix[x][y] * X)) + (image2_matrix[x][y] - (image2_matrix[x][y] * X))

                            # Przypisanie nowej wartosci
                            result_matrix[x][y] = L

            if show == True:
                    #przed sumowaniem
                    Image.fromarray(image1_matrix, "L").show()  
                    Image.fromarray(image2_matrix, "L").show()  
                    #po sumowaniu   
                    Image.fromarray(result_matrix, "L").show() 
            if save == True:
                    Image.fromarray(result_matrix, "L").save("../../Resources/Gray/Gray_Img_Sum_Result.tiff", "TIFF")  

        def multiple_const(self, const = 0, show = False, save = False):
            
            image1_matrix = self.im1
            image2_matrix = self.im2
            height = image1_matrix.shape[0]   # wysokosc
            width = image1_matrix.shape[1]    # szereoksc

            result_matrix = np.empty((height, width), dtype=np.uint8)

            for y in range(height):
                for x in range(width):  

                    L = int(image1_matrix[x][y]) 
                    if L == 255:
                        L = const
                    elif L == 0:
                        L = 0
                    else:
                        L = (int(image1_matrix[x][y]) * const)/255 

                    # Przypisanie nowej wartosci
                    result_matrix[x][y] = L

            if show == True:
                #przed sumowaniem
                Image.fromarray(image1_matrix, "L").show()  
                #po sumowaniu   
                Image.fromarray(result_matrix, "L").show() 
            if save == True:
                Image.fromarray(result_matrix, "L").save("../../Resources/Gray/Gray_Const_Multpl_Result.tiff", "TIFF")  


        def multiple_img(self, show = False, save = False):
                
                image1_matrix = self.im1
                image2_matrix = self.im2
                height = image1_matrix.shape[0]   # wysokosc
                width = image1_matrix.shape[1]    # szereoksc

                result_matrix = np.empty((height, width), dtype=np.uint8)

                for y in range(height):
                    for x in range(width):  

                        L = int(image1_matrix[x][y]) 
                        if L == 255:
                            L = image2_matrix[x][y]
                        elif L == 0:
                            L = 0
                        else:
                            L = (int(image1_matrix[x][y]) * int(image2_matrix[x][y]))/255 

                        # Przypisanie nowej wartosci
                        result_matrix[x][y] = L

                if show == True:
                    #przed sumowaniem
                    Image.fromarray(image1_matrix, "L" ).show()  
                    Image.fromarray(image2_matrix, "L").show()  
                    #po sumowaniu   
                    Image.fromarray(result_matrix, "L").show() 
                if save == True:
                    Image.fromarray(result_matrix, "L").save("../../Resources/Gray/Gray_Img_Mult_Result.tiff", "TIFF")  



#TESTY
zad2 = ArithmeticGray(image1Path = "../../Resources/Gray/Mostek.tiff", image2Path = "../../Resources/Gray/Statek.tiff")
# zad2.sum_const(const = 60, show = True, save = True)
# zad2.sum_img(show = True, save = True)
zad2.multiple_const(const = 60, show = True, save = True)
zad2.multiple_img(show = True, save = True)
