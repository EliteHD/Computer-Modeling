from PIL import Image

im = Image.open(r'OIP.jpg')
im.show()
imprueba = im
i = 0
while i < imprueba.size[0]:
    j = 0
    while j < imprueba.size[1]:
        r, g, b = imprueba.getpixel((i, j))
        rresta = 255 - r
        gresta = 255 - g
        bresta = 255 - b
        pixel = tuple([rresta, gresta, bresta])
        imprueba.putpixel((i, j), pixel)
        j += 1
    i += 1
imprueba.show()
