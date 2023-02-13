from PIL import Image
import PIL

image = Image.open(r'OIP.jpg')

altura = image.size[0]
ancho = image.size[1]

for i in range(altura):
    for j in range(ancho):
        data = image.getpixel((i,j))
        rojo=data[0]
        verde=data[1]
        azul=data[2]
        #Multiplicando los valores con rgb
        convertiragris = int(((0.299*rojo)+(0.587*verde)+(0.114*azul)))
        image.putpixel((i,j),(convertiragris,convertiragris,convertiragris))

image = image.save("Gris.jpg")