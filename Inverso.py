from PIL import Image
import PIL

image = Image.open(r'Gris.jpg')

altura = image.size[0]
ancho = image.size[1]

for x in range(altura):
    for y in range(ancho):
        data = image.getpixel((x,y))
        rojo=data[0]
        verde=data[1]
        azul=data[2]
        #Multiplicando los valores con rgb
        convertir = int((255-rojo)+(255-verde)+(255-azul))
        image.putpixel((x,y),(convertir,convertir,convertir))

image = image.save("Inverso2.jpg")