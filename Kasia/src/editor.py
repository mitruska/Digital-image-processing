image_matrix = self.im1
width = image_matrix.shape[1]    # szereoksc
height = image_matrix.shape[0]   # wysokosc

result_matrix = np.zeros((height, width), dtype=np.uint8)

f_min = 0
f_max = 0

for y in range(height):
    for x in range(width):  
        # Obliczanie sumy
        L = int(image1_matrix[y][x]) + int(const)

        Q_max = L
        D_max = 0
        X = 0

        # Sprawdzenie czy przekracza zakres
        if Q_max > 255:
            D_max = Q_max - 255
            X = (D_max/255)

        # Obliczenie sumy z uwzglednieniem zakresu
        L = (image1_matrix[y][x] - (image1_matrix[y][x] * X)) + (const - (const * X))

        # Zaokroglenie do najblizszej wartosci calkowitej z gory
        # i przypisanie wartosci
        result_matrix[y][x] = math.ceil(L)

        #Poszukiwanie minimum i maksimum
        if f_min > L:
            f_min = L
        if f_max < L:
            f_max = L
            
norm_matrix = np.zeros((height, width), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        norm_matrix[y][x] = 255 * (result_matrix[y][x] 
        
    
