from PIL import Image
import numpy as np
import math

class MorphoBin:
        def __init__(self, im1Name = "1", image1Path = None):
                if image1Path is not None:
                        image = Image.open(image1Path)
                        self.im1 = np.array(image)
                        self.im1Name = im1Name

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
                        #TIFF
                        Image.fromarray(image_matrix).save("../../Resources/Results/TIFF/" + self.im1Name + "Bin_E_Original.tiff", "TIFF") 
                        Image.fromarray(result_matrix).save("../../Resources/Results/TIFF/" + self.im1Name + "Bin_E_Result.tiff", "TIFF")  
                        #PNG  
                        Image.fromarray(image_matrix).save("../../Resources/Results/PNG/" + self.im1Name + "Bin_E_Original.png", "PNG") 
                        Image.fromarray(result_matrix).save("../../Resources/Results/PNG/" + self.im1Name + "Bin_E_Result.png", "PNG")  

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
                        #TIFF
                        Image.fromarray(image_matrix).save("../../Resources/Results/TIFF/" + self.im1Name + "Bin_D_Original.tiff", "TIFF") 
                        Image.fromarray(result_matrix).save("../../Resources/Results/TIFF/" + self.im1Name + "Bin_D_Result.tiff", "TIFF")  
                        #PNG  
                        Image.fromarray(image_matrix).save("../../Resources/Results/PNG/" + self.im1Name + "Bin_D_Original.png", "PNG") 
                        Image.fromarray(result_matrix).save("../../Resources/Results/PNG/" + self.im1Name + "Bin_D_Result.png", "PNG")  


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
                        Image.fromarray(e_result_matrix).show()                         
                        Image.fromarray(d_result_matrix).show() 
                if save == True:
                        #TIFF
                        Image.fromarray(image_matrix).save("../../Resources/Results/TIFF/" + self.im1Name + "Bin_Op_Original.tiff", "TIFF") 
                        Image.fromarray(e_result_matrix).save("../../Resources/Results/TIFF/" + self.im1Name + "Bin_Op_E_Result.tiff", "TIFF")  
                        Image.fromarray(d_result_matrix).save("../../Resources/Results/TIFF/" + self.im1Name + "Bin_Op_ED_Result.tiff", "TIFF")
                        #PNG  
                        Image.fromarray(image_matrix).save("../../Resources/Results/PNG/" + self.im1Name + "Bin_Op_Original.png", "PNG") 
                        Image.fromarray(e_result_matrix).save("../../Resources/Results/PNG/" + self.im1Name + "Bin_Op_E_Result.png", "PNG")  
                        Image.fromarray(d_result_matrix).save("../../Resources/Results/PNG/" + self.im1Name + "Bin_Op_ED_Result.png", "PNG")  


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
                        Image.fromarray(d_result_matrix).show()                         
                        Image.fromarray(e_result_matrix).show() 
                if save == True:
                        #TIFF
                        Image.fromarray(image_matrix).save("../../Resources/Results/TIFF/" + self.im1Name + "Bin_Cl_Original.tiff", "TIFF") 
                        Image.fromarray(d_result_matrix).save("../../Resources/Results/TIFF/" + self.im1Name + "Bin_Cl_D_Result.tiff", "TIFF")  
                        Image.fromarray(e_result_matrix).save("../../Resources/Results/TIFF/" + self.im1Name + "Bin_Cl_DE_Result.tiff", "TIFF")
                        #PNG  
                        Image.fromarray(image_matrix).save("../../Resources/Results/PNG/" + self.im1Name + "Bin_Cl_Original.png", "PNG") 
                        Image.fromarray(d_result_matrix).save("../../Resources/Results/PNG/" + self.im1Name + "Bin_Cl_D_Result.png", "PNG")  
                        Image.fromarray(e_result_matrix).save("../../Resources/Results/PNG/" + self.im1Name + "Bin_Cl_DE_Result.png", "PNG")  

# mor1 = MorphoBin(image1Path = "../../Resources/Binary/Circles.tiff")
# mor1.erozion(True, True)
# mor1.dilation(True, True)
# mor1.opening(True, True)
# mor1.closing(True, True)

# mor2 = MorphoBin("2", image1Path = "../../Resources/Binary/Kwadrat.tiff")
# mor2.erozion(True, True)
# mor2.dilation(True, True)
# mor2.opening(True, True)
# mor2.closing(True, True)