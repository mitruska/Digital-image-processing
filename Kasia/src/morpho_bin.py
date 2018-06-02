from PIL import Image
import numpy as np
import math

class MorphoBin:
        def __init__(self, image1Path = None, image2Path = None):
                if image1Path is not None:
                        image = Image.open(image1Path)
                        self.im1 = np.array(image)
                if image2Path is not None:
                        # self.im2Name = self.getName(image2Path)
                        self.im2 = np.array(Image.open(image2Path))

        def erozion(self, show = False, save = False):

                image_matrix = self.im1
                width = image_matrix.shape[1]    # szereoksc
                height = image_matrix.shape[0]   # wysokosc

                result_matrix = np.zeros((height, width), dtype=np.uint8)

                for y in range(height):
                        for x in range(width):  
                                #przyjeto, ze wartosci wykraczajace poza zakres sa biale (maja wartosc 255)
                                neighbour_pix = [255, 255, 255, 255]

                                if x - 1 > 0:
                                        neighbour_pix[0]=(image_matrix[y][x-1][0])
                                if y - 1 > 0:
                                        neighbour_pix[1]=(image_matrix[y-1][x][0])
                                if x + 1 < width:
                                        neighbour_pix[2]=(image_matrix[y][x+1][0])
                                if y + 1 < height:
                                        neighbour_pix[3]=(image_matrix[y+1][x][0])

                                if 255 in neighbour_pix:
                                        result_matrix[y][x] = 255 #bialy
                                else:
                                        result_matrix[y][x] = 0 #czarny    

                if show == True:
                        #przed 
                        Image.fromarray(image_matrix).show()  
                        #po    
                        Image.fromarray(result_matrix).show() 
                if save == True:
                        Image.fromarray(result_matrix).save("../../Resources/Binary/Bin_Ero_Result.tiff", "TIFF")  


        def dilation(self, show = False, save = False):
    
                image_matrix = self.im1
                width = image_matrix.shape[1]    # szereoksc
                height = image_matrix.shape[0]   # wysokosc

                result_matrix = np.zeros((height, width), dtype=np.uint8)

                for y in range(height):
                        for x in range(width):  
                                neighbour_pix = [255, 255, 255, 255]

                                if x - 1 > 0:
                                        neighbour_pix[0]=(image_matrix[y][x-1][0])
                                if y - 1 > 0:
                                        neighbour_pix[1]=(image_matrix[y-1][x][0])
                                if x + 1 < width:
                                        neighbour_pix[2]=(image_matrix[y][x+1][0])
                                if y + 1 < height:
                                        neighbour_pix[3]=(image_matrix[y+1][x][0])

                                if 0 in neighbour_pix:
                                        result_matrix[y][x] = 0
                                else:
                                        result_matrix[y][x] = 255          

                if show == True:
                        #przed 
                        Image.fromarray(image_matrix).show()  
                        #po    
                        Image.fromarray(result_matrix).show() 
                if save == True:
                        Image.fromarray(result_matrix).save("../../Resources/Binary/Bin_Dil_Result.tiff", "TIFF")  


        def opening(self, show = False, save = False):
    
                image_matrix = self.im1
                width = image_matrix.shape[1]    # szereoksc
                height = image_matrix.shape[0]   # wysokosc

                e_result_matrix = np.zeros((height, width), dtype=np.uint8)
                d_result_matrix = np.zeros((height, width), dtype=np.uint8)
                
                #erozja
                for y in range(height):
                        for x in range(width):  
                                neighbour_pix = [255, 255, 255, 255]

                                if x - 1 > 0:
                                        neighbour_pix[0]=(image_matrix[y][x-1][0])
                                if y - 1 > 0:
                                        neighbour_pix[1]=(image_matrix[y-1][x][0])
                                if x + 1 < width:
                                        neighbour_pix[2]=(image_matrix[y][x+1][0])
                                if y + 1 < height:
                                        neighbour_pix[3]=(image_matrix[y+1][x][0])

                                if 255 in neighbour_pix:
                                        e_result_matrix[y][x] = 255
                                else:
                                        e_result_matrix[y][x] = 0 

                Image.fromarray(e_result_matrix).show()
                #dylacja
                for y in range(height):
                        for x in range(width):  
                                neighbour_pix = [255, 255, 255, 255]

                                if x - 1 > 0:
                                        neighbour_pix[0]=(e_result_matrix[y][x-1])
                                if y - 1 > 0:
                                        neighbour_pix[1]=(e_result_matrix[y-1][x])
                                if x + 1 < width:
                                        neighbour_pix[2]=(e_result_matrix[y][x+1])
                                if y + 1 < height:
                                        neighbour_pix[3]=(e_result_matrix[y+1][x])

                                if 0 in neighbour_pix:
                                        d_result_matrix[y][x] = 0
                                else:
                                        d_result_matrix[y][x] = 255         

                if show == True:
                        #przed 
                        Image.fromarray(image_matrix).show()  
                        #po    
                        Image.fromarray(d_result_matrix).show() 
                if save == True:
                        Image.fromarray(d_result_matrix).save("../../Resources/Binary/Bin_Op_Result.tiff", "TIFF")  


        def closing(self, show = False, save = False):
        
                image_matrix = self.im1
                width = image_matrix.shape[1]    # szereoksc
                height = image_matrix.shape[0]   # wysokosc

                e_result_matrix = np.zeros((height, width), dtype=np.uint8)
                d_result_matrix = np.zeros((height, width), dtype=np.uint8)
                
                #dylacja
                for y in range(height):
                        for x in range(width):  
                                neighbour_pix = [255, 255, 255, 255]

                                if x - 1 > 0:
                                        neighbour_pix[0]=(image_matrix[y][x-1][0])
                                if y - 1 > 0:
                                        neighbour_pix[1]=(image_matrix[y-1][x][0])
                                if x + 1 < width:
                                        neighbour_pix[2]=(image_matrix[y][x+1][0])
                                if y + 1 < height:
                                        neighbour_pix[3]=(image_matrix[y+1][x][0])

                                if 0 in neighbour_pix:
                                        d_result_matrix[y][x] = 0
                                else:
                                        d_result_matrix[y][x] = 255

                Image.fromarray(e_result_matrix).show()
                
                #erozja
                for y in range(height):
                        for x in range(width):  
                                neighbour_pix = [255, 255, 255, 255]

                                if x - 1 > 0:
                                        neighbour_pix[0]=(d_result_matrix[y][x-1])
                                if y - 1 > 0:
                                        neighbour_pix[1]=(d_result_matrix[y-1][x])
                                if x + 1 < width:
                                        neighbour_pix[2]=(d_result_matrix[y][x+1])
                                if y + 1 < height:
                                        neighbour_pix[3]=(d_result_matrix[y+1][x])

                                if 255 in neighbour_pix:
                                        e_result_matrix[y][x] = 255
                                else:
                                        e_result_matrix[y][x] = 0         

                if show == True:
                        #przed 
                        Image.fromarray(image_matrix).show()  
                        #po    
                        Image.fromarray(e_result_matrix).show() 
                if save == True:
                        Image.fromarray(e_result_matrix).save("../../Resources/Binary/Bin_Op_Result.tiff", "TIFF")  

zad3 = MorphoBin(image1Path = "../../Resources/Binary/Kwadrat.tif")
zad3.erozion(True, True)
zad3.dilation(True, True)
# zad3.opening(True, True)