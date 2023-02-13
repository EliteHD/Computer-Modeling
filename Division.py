from PIL import Image

image = Image.open(r'OIP.jpg')

altura = image.size[0]
ancho = image.size[1]
valor = int(input("Introduzca el valor a Dividir: "))
for i in range(altura):
    for j in range(ancho):
        data = image.getpixel((i,j))
        rojo=data[0]
        verde=data[1]
        azul=data[2]
        dividir = int(((abs(rojo/valor))+(abs(verde/valor))+(abs(azul/valor))))
        image.putpixel((i,j),(dividir,dividir,dividir))
image.show()
image = image.save("Divison.jpg")