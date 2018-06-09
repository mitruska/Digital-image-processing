from PIL import Image
import numpy as np
import math

class ArithmeticGray:
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
        width = image_matrix.shape[1]    # szereoksc
        height = image_matrix.shape[0]   # wysokosc

        result_matrix = np.zeros((width, height), dtype=np.uint8)

        # Inicjalizacja zmiennych
        Q_max = 0
        D_max = 0
        X = 0
        f_min = 255
        f_max = 0

        for y in range(height):
            for x in range(width):  
                # Obliczanie sumy
                L = int(image_matrix[x][y]) + int(const)

                # Poszukiwanie maksimum
                if Q_max < L:
                    Q_max = L

        # Sprawdzenie czy przekracza zakres
        if Q_max > 255:
            D_max = Q_max - 255
            X = (D_max/255)

        # Obliczenie sumy z uwzglednieniem zakresu
        for y in range(height):
            for x in range(width): 
                L = (image_matrix[x][y] - (image_matrix[x][y] * X)) + (const - (const * X))

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y] = math.ceil(L)

                # Poszukiwanie minimum i maksimum
                if f_min > L:
                    f_min = L
                if f_max < L:
                    f_max = L
    
        # Normalizacja
        norm_matrix = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y] = 255 * ((result_matrix[x][y] - f_min) / (f_max - f_min))

        if show == True:
            #przed sumowaniem
            Image.fromarray(image1_matrix, "L").show()  
            #po sumowaniu   
            Image.fromarray(result_matrix, "L").show() 
            #po normalizacji
            Image.fromarray(norm_matrix, "L").show() 

        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Const_Sum_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Const_Sum_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Const_Sum_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Const_Sum_Original.png", "PNG")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Const_Sum_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Const_Sum_Result_Norm.png", "PNG") 

    def sum_img(self, show = False, save = False):
        
        image1_matrix = self.im1
        image2_matrix = self.im2
        height = image1_matrix.shape[0]   # wysokosc
        width = image1_matrix.shape[1]    # szereoksc

        result_matrix = np.zeros((height, width), dtype=np.uint8)

        # Inicjalizacja zmiennych
        Q_max = 0
        D_max = 0
        X = 0
        f_min = 255
        f_max = 0

        for y in range(height):
            for x in range(width):  

                # Obliczanie sumy
                L = int(image1_matrix[x][y]) + int(image2_matrix[x][y])

                # Poszukiwanie maksimum
                if Q_max < L:
                    Q_max = L

        # Sprawdzenie czy przekracza zakres
        if Q_max > 255:
            D_max = Q_max - 255
            X = (D_max/255)

        # Obliczenie sumy z uwzglednieniem zakresu
        for y in range(height):
            for x in range(width): 
                L = (image1_matrix[x][y] - (image1_matrix[x][y] * X)) + (image2_matrix[x][y] - (image2_matrix[x][y] * X))

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y] = math.ceil(L)
                
                # Poszukiwanie minimum i maksimum
                if f_min > L:
                    f_min = L
                if f_max < L:
                    f_max = L

        # Normalizacja
        norm_matrix = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y] = 255 * ((result_matrix[x][y] - f_min) / (f_max - f_min))

        if show == True:
            #przed sumowaniem
            Image.fromarray(image1_matrix, "L").show()
            Image.fromarray(image2_matrix, "L").show()  
            #po sumowaniu   
            Image.fromarray(result_matrix, "L").show() 
            #po normalizacji
            Image.fromarray(norm_matrix, "L").show() 

        if save == True:
            #TIFF
            Image.fromarray(image1_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img1_Sum_Original.tiff", "TIFF")  
            Image.fromarray(image2_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img2_Sum_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img_Sum_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img_Sum_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image1_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img1_Sum_Original.png", "PNG")  
            Image.fromarray(image2_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img2_Sum_Original.png", "PNG")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img_Sum_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img_Sum_Result_Norm.png", "PNG") 

    def multiply_const(self, const = 0, show = False, save = False):
        
        image1_matrix = self.im1
        height = image1_matrix.shape[0]   # wysokosc
        width = image1_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width), dtype=np.uint8)

        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0

        # Mnozenie 
        for y in range(height):
            for x in range(width):  

                L = int(image1_matrix[x][y]) 
                if L == 255:
                    L = const
                elif L == 0:
                    L = 0
                else:
                    L = (int(image1_matrix[x][y]) * const)/255 

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y] = math.ceil(L)

                # Poszukiwanie minimum i maksimum
                if f_min > L:
                    f_min = L
                if f_max < L:
                    f_max = L

        # Normalizacja
        norm_matrix = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y] = 255 * ((result_matrix[x][y] - f_min) / (f_max - f_min))

        if show == True:
            #przed 
            Image.fromarray(image1_matrix, "L").show()  
            #po    
            Image.fromarray(result_matrix, "L").show() 
            #po normalizacji
            Image.fromarray(norm_matrix, "L").show() 

        if save == True:
            #TIFF
            Image.fromarray(image1_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Const_Multipl_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Const_Multipl_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Const_Multipl_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image1_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Const_Multipl_Original.png", "PNG")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Const_Multipl_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Const_Multipl_Result_Norm.png", "PNG") 

    def multiply_img(self, show = False, save = False):
            
        image1_matrix = self.im1
        image2_matrix = self.im2
        height = image1_matrix.shape[0]   # wysokosc
        width = image1_matrix.shape[1]    # szereoksc

        result_matrix = np.zeros((height, width), dtype=np.uint8)

        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0

        for y in range(height):
            for x in range(width):  

                L = int(image1_matrix[x][y]) 
                if L == 255:
                    L = image2_matrix[x][y]
                elif L == 0:
                    L = 0
                else:
                    L = (int(image1_matrix[x][y]) * int(image2_matrix[x][y]))/255 

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y] = math.ceil(L)
                                
                # Poszukiwanie minimum i maksimum
                if f_min > L:
                    f_min = L
                if f_max < L:
                    f_max = L

        # Normalizacja
        norm_matrix = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y] = 255 * ((result_matrix[x][y] - f_min) / (f_max - f_min))
               
        if show == True:
            #przed 
            Image.fromarray(image1_matrix, "L").show()
            Image.fromarray(image2_matrix, "L").show()  
            #po    
            Image.fromarray(result_matrix, "L").show() 
            #po normalizacji
            Image.fromarray(norm_matrix, "L").show() 

        if save == True:
            #TIFF
            Image.fromarray(image1_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img1_Multipl_Original.tiff", "TIFF")  
            Image.fromarray(image2_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img2_Multipl_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img_Multipl_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img_Multipl_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image1_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img1_Multipl_Original.png", "PNG")  
            Image.fromarray(image2_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img2_Multipl_Original.png", "PNG")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img_Multipl_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img_Multipl_Result_Norm.png", "PNG") 

    def mix_alfa(self, alfa = 0.5, show = False, save = False):
        
        image1_matrix = self.im1
        image2_matrix = self.im2
        height = image1_matrix.shape[0]   # wysokosc
        width = image1_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width), dtype=np.uint8)

        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0

        for y in range(height):
            for x in range(width):  

                L = float(image1_matrix[x][y]) * alfa + (1-alfa) * float(image2_matrix[x][y])

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y] = math.ceil(L)

                # Poszukiwanie minimum i maksimum
                if f_min > L:
                    f_min = L
                if f_max < L:
                    f_max = L

        # Normalizacja
        norm_matrix = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y] = 255 * ((result_matrix[x][y] - f_min) / (f_max - f_min))
               

        if show == True:
            #przed sumowaniem
            Image.fromarray(image1_matrix, "L").show()
            Image.fromarray(image2_matrix, "L").show()  
            #po sumowaniu   
            Image.fromarray(result_matrix, "L").show() 
            #po normalizacji
            Image.fromarray(norm_matrix, "L").show() 

        if save == True:
            #TIFF
            Image.fromarray(image1_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img1_Mix_Original.tiff", "TIFF")  
            Image.fromarray(image2_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img2_Mix_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img_Mix_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Img_Mix_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image1_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img1_Mix_Original.png", "PNG")  
            Image.fromarray(image2_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img2_Mix_Original.png", "PNG")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img_Mix_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Img_Mix_Result_Norm.png", "PNG") 

    def pow_img(self, alfa = 1, show = False, save = False):
        
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.zeros((height, width), dtype=np.uint8)

        # Inicjalizacja zmiennych
        f_min = 255
        f_max = 0

        for y in range(height):
            for x in range(width):  
                
                L = int(image_matrix[x][y])
                if L == 255:
                    L = 255
                elif L == 0:
                    L = 0
                else:
                    # print("Before pow", L)
                    L = math.pow(int(image_matrix[x][y]), alfa)/255

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y] = math.ceil(L)

                # Poszukiwanie minimum i maksimum
                if f_min > math.ceil(L):
                    f_min = math.ceil(L)
                if f_max < math.ceil(L):
                    f_max = math.ceil(L)
        
        # Normalizacja
        norm_matrix = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                norm_matrix[x][y] = 255 * ((result_matrix[x][y] - f_min) / (f_max - f_min))
               

        if show == True:
            #przed 
            Image.fromarray(image_matrix, "L").show()  
            #po    
            Image.fromarray(result_matrix, "L").show() 
            #po normalizacji
            Image.fromarray(norm_matrix, "L").show() 

        if save == True:
            #TIFF
            Image.fromarray(image_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Pow_Original.tiff", "TIFF")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Pow_Result.tiff", "TIFF")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/TIFF/" + self.im1Name + "Gray_Const_Multipl_Result_Norm.tiff", "TIFF")  
            #PNG
            Image.fromarray(image_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Pow_Original.png", "PNG")  
            Image.fromarray(result_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Pow_Result.png", "PNG")  
            Image.fromarray(norm_matrix, "L").save("../../Resources/Results/PNG/" + self.im1Name + "Gray_Pow_Result_Norm.png", "PNG") 

    #TO DO
    def div_const(self, const = 0, show = False, save = False):
        
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width), dtype=np.uint8)
        for y in range(height):
            for x in range(width):  

                L = int(image_matrix[x][y]) 

                if const == 0:
                    const = 1
                else:
                    L = (float(image_matrix[x][y]) * float(1/const) * 255 )

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y] = math.ceil(L)

        # for y in range(height):
        #     for x in range(width):  
                
        #         #TO ASK

        #         # L = int(image1_matrix[x][y]) + int(const)
        #         L = float(image_matrix[x][y]) / float(const)
                
        #         # L = (int(image1_matrix[x][y]) * 255

        #         # Zaokroglenie do najblizszej wartosci calkowitej z gory
        #         # i przypisanie wartosci
        #         result_matrix[x][y] = math.ceil(L)

        if show == True:
            #przed 
            Image.fromarray(image_matrix, "L").show()  
            #po    
            Image.fromarray(result_matrix, "L").show() 
        if save == True:
            Image.fromarray(result_matrix, "L").save("../../Resources/Gray/Gray_Const_Multpl_Result.tiff", "TIFF")  


    #TO DO
    def div_img(self, show = False, save = False):
        
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

                        Q_L = (L * 255) / Q_max

        if show == True:
            #przed 
            Image.fromarray(image_matrix, "L" ).show()  
            #po    
            Image.fromarray(result_matrix, "L").show() 
        if save == True:
            Image.fromarray(result_matrix, "L").save("../../Resources/Gray/Gray_Img_Mult_Result.tiff", "TIFF")  


    def sqrt_img(self, alfa = 1, show = False, save = False):
        
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width), dtype=np.uint8)

        for y in range(height):
            for x in range(width):  
                
                L = int(image_matrix[x][y])
                if L == 0:
                    L = 0
                else:
                    # print("Before pow", L)
                    L = math.sqrt(int(image_matrix[x][y]), alfa)
                    
                    Q_max = L
                    D_max = 0
                    X = 0

                    # Sprawdzenie czy przekracza zakres
                    if Q_max > 255:
                        D_max = Q_max - 255
                        X = (D_max/255)

                    # Normalizacja
                    L = (L - L * X)

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y] = math.ceil(L)


    def log_img(self, alfa = 1, show = False, save = False):
        
        image_matrix = self.im1
        height = image_matrix.shape[0]   # wysokosc
        width = image_matrix.shape[1]    # szereoksc

        result_matrix = np.empty((height, width), dtype=np.uint8)

        for y in range(height):
            for x in range(width):  

                L = int(image_matrix[x][y]) 

                if L == 0:
                    L = 0
                else:
                    L = math.log(1 + L)

                # Zaokroglenie do najblizszej wartosci calkowitej z gory
                # i przypisanie wartosci
                result_matrix[x][y] = math.ceil(L)

        if show == True:
            #przed 
            Image.fromarray(image_matrix, "L").show()  
            #po    
            Image.fromarray(result_matrix, "L").show() 
        if save == True:
            Image.fromarray(result_matrix, "L").save("../../Resources/Gray/Gray_Const_Multpl_Result.tiff", "TIFF")  


#TESTY

arm1 = ArithmeticGray(image1Path = "../../Resources/Gray/Zegarek.tiff", image2Path = "../../Resources/Gray/Gentelman.tiff")
# # # # arm1.sum_const(const = 50, show = True, save = True)
# # # # arm1.sum_img(show = True, save = True)
# # arm1.multiply_const(const = 50, show = True, save = True)
# arm1.multiply_img(show = True, save = True)
# arm1.mix_alfa(alfa = 0.5, show = True, save = True)
arm1.pow_img(alfa = 2, show = True, save = True)






arm2 = ArithmeticGray(im1Name_ = "2", image1Path = "../../Resources/Gray/Pirat.tiff", image2Path = "../../Resources/Gray/Statek.tiff")
# # # arm2.sum_const(const = 100, show = True, save = True)
# # # arm2.sum_img(show = True, save = True)
# arm2.multiply_const(const = 100, show = True, save = True)
# arm2.multiply_img(show = True, save = True)
# arm2.mix_alfa(alfa = 0.8, show = True, save = True)
arm2.pow_img(alfa = 2, show = True, save = True)





# zad2.sum_img(show = True, save = True)
# zad2.multiply_const(const = 60, show = True, save = True)
# zad2.multiply_img(show = True, save = True)
# zad2.mix_alfa(alfa = 0.3, show = True, save = True)
# zad2.pow_img(alfa = 2, show = True, save = True)
# zad2.div_const(const = 60, show = True, save = True)
