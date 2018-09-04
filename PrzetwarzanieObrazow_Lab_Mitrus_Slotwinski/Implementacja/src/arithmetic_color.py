from PIL import Image
import numpy as np
import math


class ArithmeticColor:

    def __init__(self, im1Name_ = "1", im2Name_ = "2", image1Path = None, image2Path = None):
            if image1Path is not None:
                self.im1Name = im1Name_
                self.im1 = np.array(Image.open(image1Path))
            if image2Path is not None:
                self.im2Name = im2Name_
                self.im2 = np.array(Image.open(image2Path))

    # Sumowanie okreslonej stalej z obrazem
    def sum_const(self, const = 0, show = False, save = False):
        
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((width, height, 3), dtype=np.uint8)

        # Inicjalizacja zmiennych
        Q_max = 0
        D_max = 0
        X = 0
        f_min = 255
        f_max = 0

        for y in range(height):
            for x in range(width):  

                # Obliczanie sum
                R = int(image_matrix[x][y][0]) + int(const)
                G = int(image_matrix[x][y][1]) + int(const)
                B = int(image_matrix[x][y][2]) + int(const)

                # Poszukiwanie maksimum               
                if Q_max < max([R, G, B]):
                    Q_max = max([R, G, B])

        # Sprawdzenie czy maksimum przekracza zakres
        if Q_max > 255:
            D_max = Q_max - 255
            X = (D_max/255) # Obliczenie proporcji
        
        # Obliczenie sum z uwzglednieniem zakresu
        for y in range(height):
            for x in range(width): 
                R = (image_matrix[x][y][0] - (image_matrix[x][y][0] * X)) + (const - (const * X))
                G = (image_matrix[x][y][1] - (image_matrix[x][y][1] * X)) + (const - (const * X))
                B = (image_matrix[x][y][2] - (image_matrix[x][y][2] * X)) + (const - (const * X))

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y][0] = math.ceil(R)
                result_matrix[x][y][1] = math.ceil(G)
                result_matrix[x][y][2] = math.ceil(B)

                # Poszukiwanie minimum i maksimum                
                if f_min > min([R, G, B]):
                    f_min = min([R, G, B])
                if f_max < max([R, G, B]):
                    f_max = max([R, G, B])

        # Normalizacja
        norm_matrix = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y][0] = 255 * ((result_matrix[x][y][0] - f_min) / (f_max - f_min))
                norm_matrix[x][y][1] = 255 * ((result_matrix[x][y][1] - f_min) / (f_max - f_min))
                norm_matrix[x][y][2] = 255 * ((result_matrix[x][y][2] - f_min) / (f_max - f_min))

        if show == True:
            #przed sumowaniem
            Image.fromarray(image_matrix, "RGB").show()  
            #po sumowaniu   
            Image.fromarray(result_matrix, "RGB").show()
            #po normalizacji
            Image.fromarray(norm_matrix, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Const_Sum_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Const_Sum_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Const_Sum_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Const_Sum_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Const_Sum_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Const_Sum_Result_Norm.png", "PNG")  


    def sum_img(self, show = False, save = False):
        
        image1_matrix = self.im1
        image2_matrix = self.im2
        height = image1_matrix.shape[0]   # wysokosc
        width = image1_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width, 3), dtype=np.uint8)

        # Inicjalizacja zmiennych
        Q_max = 0
        D_max = 0
        X = 0
        f_min = 255
        f_max = 0

        for y in range(height):
            for x in range(width):  

                # Obliczanie sum
                R = int(image1_matrix[x][y][0]) + int(image2_matrix[x][y][0])
                G = int(image1_matrix[x][y][1]) + int(image2_matrix[x][y][1])
                B = int(image1_matrix[x][y][2]) + int(image2_matrix[x][y][2])
                
                # Poszukiwanie maksimum               
                if Q_max < max([R, G, B]):
                    Q_max = max([R, G, B])

        # Sprawdzenie czy maximum przekracza zakres
        if Q_max > 255:
            D_max = Q_max - 255
            X = (D_max/255) # Obliczenie proporcji
        
        # Obliczenie sum z uwzglednieniem zakresu
        for y in range(height):
            for x in range(width): 
                R = (image1_matrix[x][y][0] - (image1_matrix[x][y][0] * X)) + (image2_matrix[x][y][0] - (image2_matrix[x][y][0] * X))
                G = (image1_matrix[x][y][1] - (image1_matrix[x][y][1] * X)) + (image2_matrix[x][y][1] - (image2_matrix[x][y][1] * X))
                B = (image1_matrix[x][y][2] - (image1_matrix[x][y][2] * X)) + (image2_matrix[x][y][2] - (image2_matrix[x][y][2] * X))

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y][0] = math.ceil(R)
                result_matrix[x][y][1] = math.ceil(G)
                result_matrix[x][y][2] = math.ceil(B)

                # Poszukiwanie minimum i maksimum                
                if f_min > min([R, G, B]):
                    f_min = min([R, G, B])
                if f_max < max([R, G, B]):
                    f_max = max([R, G, B])
        
        # Normalizacja
        norm_matrix = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y][0] = 255 * ((result_matrix[x][y][0] - f_min) / (f_max - f_min))
                norm_matrix[x][y][1] = 255 * ((result_matrix[x][y][1] - f_min) / (f_max - f_min))
                norm_matrix[x][y][2] = 255 * ((result_matrix[x][y][2] - f_min) / (f_max - f_min))

        if show == True:
            #przed sumowaniem
            Image.fromarray(image1_matrix, "RGB").show()
            Image.fromarray(image2_matrix, "RGB").show()   
            #po sumowaniu   
            Image.fromarray(result_matrix, "RGB").show()
            #po normalizacji
            Image.fromarray(norm_matrix, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Sum_Img1_Original.tiff", "TIFF")  
            Image.fromarray(image2_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Sum_Img2_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Sum_Img_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Sum_Img_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Sum_Img1_Original.png", "PNG")  
            Image.fromarray(image2_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Sum_Img2_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Sum_Img_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Sum_Img_Result_Norm.png", "PNG")  

    def multiply_const(self, const = 0, show = False, save = False):
        
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width, 3), dtype=np.uint8)

        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0

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

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y][0] = math.ceil(R)
                result_matrix[x][y][1] = math.ceil(G)
                result_matrix[x][y][2] = math.ceil(B)

                # Poszukiwanie minimum i maksimum                
                if f_min > min([R, G, B]):
                    f_min = min([R, G, B])
                if f_max < max([R, G, B]):
                    f_max = max([R, G, B])

        # Normalizacja
        norm_matrix = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y][0] = 255 * ((result_matrix[x][y][0] - f_min) / (f_max - f_min))
                norm_matrix[x][y][1] = 255 * ((result_matrix[x][y][1] - f_min) / (f_max - f_min))
                norm_matrix[x][y][2] = 255 * ((result_matrix[x][y][2] - f_min) / (f_max - f_min))


        if show == True:
            #przed sumowaniem
            Image.fromarray(image_matrix, "RGB").show()  
            #po sumowaniu   
            Image.fromarray(result_matrix, "RGB").show()
            #po normalizacji
            Image.fromarray(norm_matrix, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Const_Multipl_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Const_Multipl_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Const_Multipl_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Const_Multipl_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Const_Multipl_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Const_Multipl_Result_Norm.png", "PNG")  

    def multiply_img(self, show = False, save = False):

        image1_matrix = self.im1
        image2_matrix = self.im2
        height = image1_matrix.shape[0]   # wysokosc
        width = image1_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width, 3), dtype=np.uint8)

        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0

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

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y][0] = math.ceil(R)
                result_matrix[x][y][1] = math.ceil(G)
                result_matrix[x][y][2] = math.ceil(B)

                # Poszukiwanie minimum i maksimum                
                if f_min > min([R, G, B]):
                    f_min = min([R, G, B])
                if f_max < max([R, G, B]):
                    f_max = max([R, G, B])

        # Normalizacja
        norm_matrix = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y][0] = 255 * ((result_matrix[x][y][0] - f_min) / (f_max - f_min))
                norm_matrix[x][y][1] = 255 * ((result_matrix[x][y][1] - f_min) / (f_max - f_min))
                norm_matrix[x][y][2] = 255 * ((result_matrix[x][y][2] - f_min) / (f_max - f_min))


        if show == True:
            #przed 
            Image.fromarray(image1_matrix, "RGB").show()
            Image.fromarray(image2_matrix, "RGB").show()   
            #po    
            Image.fromarray(result_matrix, "RGB").show()
            #po normalizacji
            Image.fromarray(norm_matrix, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Multipl_Img1_Original.tiff", "TIFF")  
            Image.fromarray(image2_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Multipl_Img2_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Multipl_Img_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Multipl_Img_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Multipl_Img1_Original.png", "PNG")  
            Image.fromarray(image2_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Multipl_Img2_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Multipl_Img_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Multipl_Img_Result_Norm.png", "PNG")  

    def mix_alfa(self, alfa = 1.0, show = False, save = False):
        
        image1_matrix = self.im1
        image2_matrix = self.im2
        height = image1_matrix.shape[0]   # wysokosc
        width = image1_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width, 3), dtype=np.uint8)

        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0

        for y in range(height):
            for x in range(width):  

                R = float(image1_matrix[x][y][0]) * alfa + (1-alfa) * float(image2_matrix[x][y][0])
                G = float(image1_matrix[x][y][1]) * alfa + (1-alfa) * float(image2_matrix[x][y][1])
                B = float(image1_matrix[x][y][2]) * alfa + (1-alfa) * float(image2_matrix[x][y][2])

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y][0] = math.ceil(R)
                result_matrix[x][y][1] = math.ceil(G)
                result_matrix[x][y][2] = math.ceil(B)

                # Poszukiwanie minimum i maksimum                
                if f_min > min([R, G, B]):
                    f_min = min([R, G, B])
                if f_max < max([R, G, B]):
                    f_max = max([R, G, B])

        # Normalizacja
        norm_matrix = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y][0] = 255 * ((result_matrix[x][y][0] - f_min) / (f_max - f_min))
                norm_matrix[x][y][1] = 255 * ((result_matrix[x][y][1] - f_min) / (f_max - f_min))
                norm_matrix[x][y][2] = 255 * ((result_matrix[x][y][2] - f_min) / (f_max - f_min))
        
        
        if show == True:
            #przed 
            Image.fromarray(image1_matrix, "RGB").show()
            Image.fromarray(image2_matrix, "RGB").show()   
            #po    
            Image.fromarray(result_matrix, "RGB").show()
            #po normalizacji
            Image.fromarray(norm_matrix, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Mix_Img1_Original.tiff", "TIFF")  
            Image.fromarray(image2_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Mix_Img2_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Mix_Img_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Mix_Img_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Mix_Img1_Original.png", "PNG")  
            Image.fromarray(image2_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Mix_Img2_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Mix_Img_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Mix_Img_Result_Norm.png", "PNG")  

    def pow_img(self, alfa = 1, show = False, save = False):
        
        image1_matrix = self.im1
        height = image1_matrix.shape[0]   # wysokosc
        width = image1_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width, 3), dtype=np.uint8)
        
        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0
        f_img_max = 0

        for y in range(height):
            for x in range(width):  

                R = int(image1_matrix[x][y][0])
                G = int(image1_matrix[x][y][1])
                B = int(image1_matrix[x][y][2])

                if f_img_max < max([R, G, B]):
                    f_img_max = max([R, G, B])

        for y in range(height):
            for x in range(width):  

                R = int(image1_matrix[x][y][0])
                G = int(image1_matrix[x][y][1])
                B = int(image1_matrix[x][y][2])

                if R == 0:
                    R = 0
                else:
                    R = 255 * (math.pow(int(image1_matrix[x][y][0]) / f_img_max, alfa))

                if G == 0:
                    G = 0
                else:
                    G = 255 * (math.pow(int(image1_matrix[x][y][1]) / f_img_max, alfa))
                
                if B == 0:
                    B = 0
                else:
                    B = 255 * (math.pow(int(image1_matrix[x][y][2]) / f_img_max, alfa))

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y][0] = math.ceil(R)
                result_matrix[x][y][1] = math.ceil(G)
                result_matrix[x][y][2] = math.ceil(B)

                # Poszukiwanie minimum i maksimum                
                if f_min > min([R, G, B]):
                    f_min = min([R, G, B])
                if f_max < max([R, G, B]):
                    f_max = max([R, G, B])

        # Normalizacja
        norm_matrix = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y][0] = 255 * ((result_matrix[x][y][0] - f_min) / (f_max - f_min))
                norm_matrix[x][y][1] = 255 * ((result_matrix[x][y][1] - f_min) / (f_max - f_min))
                norm_matrix[x][y][2] = 255 * ((result_matrix[x][y][2] - f_min) / (f_max - f_min))
        
        if show == True:
            #przed 
            Image.fromarray(image1_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
            #po normalizacji
            Image.fromarray(norm_matrix, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Pow_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Pow_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Pow_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Pow_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Pow_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Pow_Result_Norm.png", "PNG")  


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    def div_const(self, const = 0, show = False, save = False):
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width, 3), dtype=np.uint8)

        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0
        Q_max = 0
        
        for y in range(height):
            for x in range(width):  

                # Obliczanie sum
                R_S = int(image_matrix[x][y][0]) + int(const)
                G_S = int(image_matrix[x][y][1]) + int(const)
                B_S = int(image_matrix[x][y][2]) + int(const)

                # Poszukiwanie maksimum
                if Q_max < max([R_S, G_S, B_S]):
                    Q_max = max([R_S, G_S, B_S])

        for y in range(height):
            for x in range(width):  

                # Obliczanie sum
                R_S = int(image_matrix[x][y][0]) + int(const)
                G_S = int(image_matrix[x][y][1]) + int(const)
                B_S = int(image_matrix[x][y][2]) + int(const)

                Q_R = (R_S * 255)/Q_max
                Q_G = (G_S * 255)/Q_max
                Q_B = (B_S * 255)/Q_max
                    
                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y][0] = math.ceil(Q_R)
                result_matrix[x][y][1] = math.ceil(Q_G)
                result_matrix[x][y][2] = math.ceil(Q_B)

                # Poszukiwanie minimum i maksimum                
                if f_min > min([Q_R, Q_G, Q_B]):
                    f_min = min([Q_R, Q_G, Q_B])
                if f_max < max([Q_R, Q_G, Q_B]):
                    f_max = max([Q_R, Q_G, Q_B])

        # Normalizacja
        norm_matrix = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y][0] = 255 * ((result_matrix[x][y][0] - f_min) / (f_max - f_min))
                norm_matrix[x][y][1] = 255 * ((result_matrix[x][y][1] - f_min) / (f_max - f_min))
                norm_matrix[x][y][2] = 255 * ((result_matrix[x][y][2] - f_min) / (f_max - f_min))
    
        if show == True:
            #przed 
            Image.fromarray(image_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
            #po normalizacji
            Image.fromarray(norm_matrix, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Div_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Div_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Div_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Div_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Div_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Div_Result_Norm.png", "PNG")  


    def div_img(self, show = False, save = False):
        
        image1_matrix = self.im1
        image2_matrix = self.im2
        height = image1_matrix.shape[0]   # wysokosc
        width = image1_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width, 3), dtype=np.uint8)

        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0
        Q_max = 0

        for y in range(height):
            for x in range(width):  

                # Obliczanie sum
                R_S = int(image1_matrix[x][y][0]) + int(image2_matrix[x][y][0])
                G_S = int(image1_matrix[x][y][1]) + int(image2_matrix[x][y][1])
                B_S = int(image1_matrix[x][y][2]) + int(image2_matrix[x][y][2])

                # Poszukiwanie maksimum
                if Q_max < max([R_S, G_S, B_S]):
                    Q_max = max([R_S, G_S, B_S])

        for y in range(height):
            for x in range(width):  

                # Obliczanie sum
                R_S = int(image1_matrix[x][y][0]) + int(image2_matrix[x][y][0])
                G_S = int(image1_matrix[x][y][1]) + int(image2_matrix[x][y][1])
                B_S = int(image1_matrix[x][y][2]) + int(image2_matrix[x][y][2])

                Q_R = (R_S * 255)/Q_max
                Q_G = (G_S * 255)/Q_max
                Q_B = (B_S * 255)/Q_max

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y][0] = math.ceil(Q_R)
                result_matrix[x][y][1] = math.ceil(Q_G)
                result_matrix[x][y][2] = math.ceil(Q_B)

                # Poszukiwanie minimum i maksimum                
                if f_min > min([Q_R, Q_G, Q_B]):
                    f_min = min([Q_R, Q_G, Q_B])
                if f_max < max([Q_R, Q_G, Q_B]):
                    f_max = max([Q_R, Q_G, Q_B])

        # Normalizacja
        norm_matrix = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y][0] = 255 * ((result_matrix[x][y][0] - f_min) / (f_max - f_min))
                norm_matrix[x][y][1] = 255 * ((result_matrix[x][y][1] - f_min) / (f_max - f_min))
                norm_matrix[x][y][2] = 255 * ((result_matrix[x][y][2] - f_min) / (f_max - f_min))
        
        if show == True:
            #przed 
            Image.fromarray(image1_matrix, "RGB").show()
            Image.fromarray(image2_matrix, "RGB").show()   
            #po    
            Image.fromarray(result_matrix, "RGB").show()
            #po normalizacji
            Image.fromarray(norm_matrix, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Div_Img1_Original.tiff", "TIFF")  
            Image.fromarray(image2_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Div_Img2_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Div_Img_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Div_Img_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Div_Img1_Original.png", "PNG")  
            Image.fromarray(image2_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Div_Img2_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Div_Img_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Div_Img_Result_Norm.png", "PNG")  

    def sqrt_img(self, deg = 1, show = False, save = False):
        
        image1_matrix = self.im1
        height = image1_matrix.shape[0]   # wysokosc
        width = image1_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width, 3), dtype=np.uint8)
        
        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0
        f_img_max = 0

        alfa = 1/deg # Zamiana stopnia pierwiastka na ulamek

        for y in range(height):
            for x in range(width):  

                R = int(image1_matrix[x][y][0])
                G = int(image1_matrix[x][y][1])
                B = int(image1_matrix[x][y][2])

                if f_img_max < max([R, G, B]):
                    f_img_max = max([R, G, B])

        for y in range(height):
            for x in range(width):  

                R = int(image1_matrix[x][y][0])
                G = int(image1_matrix[x][y][1])
                B = int(image1_matrix[x][y][2])

                if R == 0:
                    R = 0
                else:
                    R = 255 * (math.pow(int(image1_matrix[x][y][0]) / f_img_max, alfa))

                if G == 0:
                    G = 0
                else:
                    G = 255 * (math.pow(int(image1_matrix[x][y][1]) / f_img_max, alfa))
                
                if B == 0:
                    B = 0
                else:
                    B = 255 * (math.pow(int(image1_matrix[x][y][2]) / f_img_max, alfa))

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y][0] = math.ceil(R)
                result_matrix[x][y][1] = math.ceil(G)
                result_matrix[x][y][2] = math.ceil(B)

                # Poszukiwanie minimum i maksimum                
                if f_min > min([R, G, B]):
                    f_min = min([R, G, B])
                if f_max < max([R, G, B]):
                    f_max = max([R, G, B])

        # Normalizacja
        norm_matrix = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y][0] = 255 * ((result_matrix[x][y][0] - f_min) / (f_max - f_min))
                norm_matrix[x][y][1] = 255 * ((result_matrix[x][y][1] - f_min) / (f_max - f_min))
                norm_matrix[x][y][2] = 255 * ((result_matrix[x][y][2] - f_min) / (f_max - f_min))
        
        if show == True:
            #przed 
            Image.fromarray(image1_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
            #po normalizacji
            Image.fromarray(norm_matrix, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Sqrt_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Sqrt_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Sqrt_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Sqrt_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Sqrt_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Sqrt_Result_Norm.png", "PNG")  


    def log_img(self, show = False, save = False):
        
        image1_matrix = self.im1
        image2_matrix = self.im2
        height = image1_matrix.shape[0]   # wysokosc
        width = image1_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width, 3), dtype=np.uint8)

        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0
        f_img_max = 0

        for y in range(height):
            for x in range(width):  
                
                R = int(image1_matrix[x][y][0])
                G = int(image1_matrix[x][y][1])
                B = int(image1_matrix[x][y][2])

                # Poszukiwanie maksimum                
                if f_img_max < max([R, G, B]):
                    f_img_max = max([R, G, B])

        for y in range(height):
            for x in range(width):  
                
                R = int(image1_matrix[x][y][0])
                G = int(image1_matrix[x][y][1])
                B = int(image1_matrix[x][y][2])

                if R == 0:
                    R = 0
                else:
                    R = math.log(1 + int(image1_matrix[x][y][0])) / math.log(1 + int(f_img_max)) * 255

                if G == 0:
                    G = 0
                else:
                    G = math.log(1 + int(image1_matrix[x][y][1])) / math.log(1 + int(f_img_max)) * 255
                
                if B == 0:
                    B = 0
                else:
                    B = math.log(1 + int(image1_matrix[x][y][2])) / math.log(1 + int(f_img_max)) * 255

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y][0] = math.ceil(R)
                result_matrix[x][y][1] = math.ceil(G)
                result_matrix[x][y][2] = math.ceil(B)

                # Poszukiwanie minimum i maksimum                
                if f_min > min([R, G, B]):
                    f_min = min([R, G, B])
                if f_max < max([R, G, B]):
                    f_max = max([R, G, B])


        # Normalizacja
        norm_matrix = np.zeros((width, height, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y][0] = 255 * ((result_matrix[x][y][0] - f_min) / (f_max - f_min))
                norm_matrix[x][y][1] = 255 * ((result_matrix[x][y][1] - f_min) / (f_max - f_min))
                norm_matrix[x][y][2] = 255 * ((result_matrix[x][y][2] - f_min) / (f_max - f_min))
        
        if show == True:
            #przed 
            Image.fromarray(image1_matrix, "RGB").show()  
            #po    
            Image.fromarray(result_matrix, "RGB").show()
            #po normalizacji
            Image.fromarray(norm_matrix, "RGB").show()  
        if save == True:
            #TIFF
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Log_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Log_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/TIFF/" + self.im1Name + "Color_Log_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image1_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Log_Original.png", "PNG")  
            Image.fromarray(result_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Log_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "RGB").save("../../Resources/Results/PNG/" + self.im1Name + "Color_Log_Result_Norm.png", "PNG")  


#TESTY

# carm1 = ArithmeticColor(im1Name_="1", image1Path = "../../Resources/Color/Warzywa.tiff", image2Path = "../../Resources/Color/Statek.tiff" )
# carm1.sum_const(const = 50, show = True, save = True)
# carm1.sum_img(show = True, save = True)
# carm1.multiply_const(const = 50, show = True, save = True)
# carm1.multiply_img(show = True, save = True)
# carm1.mix_alfa(alfa = 0.5, show = True, save = True)
# carm1.pow_img(alfa = 2, show = True, save = True)
# carm1.sqrt_img(deg = 2, show = True, save = True)
# carm1.log_img(True, True)
# carm1.div_const(15, True, True)
# carm1.div_img(True, True)



# carm2 = ArithmeticColor(im1Name_="2", image1Path = "../../Resources/Color/Cukierki.tiff", image2Path = "../../Resources/Color/Kobieta.tiff" )
# carm2.sum_const(const = 100, show = True, save = True)
# carm2.sum_img(show = True, save = True)
# carm2.multiply_const(const = 100, show = True, save = True)
# carm2.multiply_img(show = True, save = True)
# carm2.mix_alfa(alfa = 0.8, show = True, save = True)
# carm2.pow_img(alfa = 3, show = True, save = True)
# carm2.sqrt_img(deg = 3, show = True, save = True)
# carm2.log_img(True, True)
# carm2.div_const(3, True, True)
# carm2.div_img(True, True)



