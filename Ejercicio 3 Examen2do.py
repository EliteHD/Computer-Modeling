import numpy as np
import cv2

img = cv2.imread('Mediana.png')

h,w,c = img.shape

img2 = np.zeros([h,w,c], dtype=np.uint8)

for i in range(h):
    for j in range(w):
        img2[i,j] = img[j-1,i-1]
        img2 = img2[0:h,0:w]

cv2.imshow("imagen Original",img)
cv2.imshow("imagen con Rotada",img2)
cv2.waitKey()
cv2.destroyAllWindows()
