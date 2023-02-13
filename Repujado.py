
import numpy as np
import cv2

img = cv2.imread(r'OIP.jpg')
A = img
M = np.array([ [-2,-1,0],[-1,1,1],[0,1,2]])
M = M/1
forma = np.shape(A)

img2 = np.zeros(forma)

#KERNEL c:

for x in list(range(1, forma[0]-1)):
    for y in list(range(1,forma[1]-1)):

        suma = 0
        for i in list(range(-1,2)):
        
            for j in list(range(-1,2)):
                suma = A[x+i,y+j]*M[i-1,j-1]+suma
        img2[x,y]= abs(suma)

maxs = np.max(img2)

img2 = img2*255/maxs

img2 = img2.astype(np.uint8)

cv2.imshow("Imagen Original",A)

cv2.imshow("Imagen con Convolucion",img2)
cv2.waitKey()
cv2.destroyAllWindows()
