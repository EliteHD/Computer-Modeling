from PIL import Image
#JOSIAS DOMINGUEZ HERNANDEZ
i = Image.open("binarizado.jpg")

pixels = i.load() 
width, height = i.size

all_pixels = []
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]

        Ap = pixels[x,y]
        
        Bp = pixels[x,y]
        if(Ap == 255 and Bp == 255):
            pixels[x,y]=255
            cpixel = pixels[x, y]
            all_pixels.append(cpixel) 
        else:
            pixels[x,y] = 0
             

image = i.save("Logicas1.jpg")








