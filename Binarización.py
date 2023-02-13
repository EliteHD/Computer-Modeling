from PIL import Image
import time

def Umbralizacion(grisBase):
    tiempoIn = time.time()
    im = Image.open(r'redes.jpg')
    im.show()
    im7 = im
    i = 0
    while i < im7.size[0]:
        j = 0
        while j < im7.size[1]:
            r, g, b = im7.getpixel((i,j))
            #CONVERTIMOS LA IMAGEN EN GRISES
            gris = (r + g + b) / 3
            if gris < grisBase:
                im7.putpixel((i,j), (0,0,0))
            else:
                im7.putpixel((i,j), (255,255,255))
            j+=1
        i+=1
    im7.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos')
    im = im.save("Redes1.jpg")
Umbralizacion(80)