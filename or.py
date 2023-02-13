from PIL import Image
import time

tiempoIn = time.time()
im = Image.open('OIPbin.jpg')

imo = Image.open('OIPbin2.jpg')
im.show()
imo.show()
im7= im
Ap= imo
Bp = im

altura = im.size[0]
ancho = im.size[1]

for i in range(altura):
    for j in range(ancho):
        valor = im7.getpixel((i, j))
        valor1 = Ap.getpixel((i,j))
        valor2 = Bp.getpixel((i,j))
        
        if ((valor1 == 255 or valor2 == 255)):
            valor = 255
        else:
            valor = 0
        im7.putpixel((i, j), (valor))
        #print(f"Valor = {valor}   AP = {valor1}   BP= {valor2}")
        j += 1
    i += 1
im7.show()
tiempoFin = time.time()
print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos')
