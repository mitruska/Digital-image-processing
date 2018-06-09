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
    