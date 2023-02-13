from PIL import Image

image = Image.open(r'OIP.jpg')

altura = image.size[0]
ancho = image.size[1]
valor = int(input("Introduzca el valor a multiplicar: "))
for i in range(altura):
    for j in range(ancho):
        data = image.getpixel((i,j))
        rojo=data[0]
        verde=data[1]
        azul=data[2]
        multiplicacion = int((((rojo*valor)/2)+((verde*valor)/2)+((azul*valor)/2)))
        image.putpixel((i,j),(multiplicacion,multiplicacion,multiplicacion))
image.show()
image = image.save("Multi.jpg")