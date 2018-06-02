from PIL import Image
import numpy as np
import math

class MorphoGray:
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
                print(image_matrix)
                print(result_matrix)

                for y in range(height):
                        for x in range(width):  
                                neighbour_pix = [255, 255, 255, 255]

                                if x - 1 > 0:
                                        neighbour_pix[0]=(image_matrix[y][x-1])
                                if y - 1 > 0:
                                        neighbour_pix[1]=(image_matrix[y-1][x])
                                if x + 1 < width:
                                        neighbour_pix[2]=(image_matrix[y][x+1])
                                if y + 1 < height:
                                        neighbour_pix[3]=(image_matrix[y+1][x])

                                min_pix = min(neighbour_pix)
                                result_matrix[y][x] = min_pix
                                          

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
                print(image_matrix)
                print(result_matrix)

                for y in range(height):
                        for x in range(width):  
                                neighbour_pix = [255, 255, 255, 255]

                                if x - 1 > 0:
                                        neighbour_pix[0]=(image_matrix[y][x-1])
                                if y - 1 > 0:
                                        neighbour_pix[1]=(image_matrix[y-1][x])
                                if x + 1 < width:
                                        neighbour_pix[2]=(image_matrix[y][x+1])
                                if y + 1 < height:
                                        neighbour_pix[3]=(image_matrix[y+1][x])

                                max_pix = max(neighbour_pix)
                                result_matrix[y][x] = max_pix      

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
                                        neighbour_pix[0]=(image_matrix[y][x-1])
                                if y - 1 > 0:
                                        neighbour_pix[1]=(image_matrix[y-1][x])
                                if x + 1 < width:
                                        neighbour_pix[2]=(image_matrix[y][x+1])
                                if y + 1 < height:
                                        neighbour_pix[3]=(image_matrix[y+1][x])

                                min_pix = min(neighbour_pix)
                                e_result_matrix[y][x] = min_pix

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

                                max_pix = max(neighbour_pix)
                                d_result_matrix[y][x] = max_pix         

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
                                        neighbour_pix[0]=(image_matrix[y][x-1])
                                if y - 1 > 0:
                                        neighbour_pix[1]=(image_matrix[y-1][x])
                                if x + 1 < width:
                                        neighbour_pix[2]=(image_matrix[y][x+1])
                                if y + 1 < height:
                                        neighbour_pix[3]=(image_matrix[y+1][x])

                                max_pix = max(neighbour_pix)
                                d_result_matrix[y][x] = max_pix   

                Image.fromarray(d_result_matrix).show()
                
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

                                min_pix = min(neighbour_pix)
                                e_result_matrix[y][x] = min_pix         

                if show == True:
                        #przed 
                        Image.fromarray(image_matrix).show()  
                        #po    
                        Image.fromarray(e_result_matrix).show() 
                if save == True:
                        Image.fromarray(e_result_matrix).save("../../Resources/Gray/Gray_Op_Result.tiff", "TIFF")  

zad3 = MorphoGray(image1Path = "../../Resources/Gray/Statek.tiff")
# zad3.erozion(True, True)
# zad3.dilation(True, True)
zad3.opening(True, True)