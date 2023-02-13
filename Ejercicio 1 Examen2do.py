import numpy as np
import cv2
# JOSIAS DOMINGUEZ HERNANDEZ
img = cv2.imread('grispimienta.png', 0) 
A = img

M = np.array([[35,35,35],[35,35,35],[35,35,35]])
M = M/9

forma = np.shape(A)
img2 = np.zeros(forma)

for x in list(range(1, forma[0]-1)):
    for y in list(range(1,forma[1]-1)):
        dataa = [img[x-1, y-1],img[x-1, y],img[x-1, y + 1], img[x, y-1], img[x, y], img[x, y + 1], img[x + 1, y-1], img[x + 1, y], img[x + 1, y + 1]]
        dataa = sorted(dataa)
        img2[x,y]= dataa[4]

img2 = img2.astype(np.uint8)
cv2.imshow("imagen Original",A)
cv2.imshow("imagen con Mediana",img2)
cv2.imwrite("Mediana.png",img2)
cv2.waitKey()
cv2.destroyAllWindows()

