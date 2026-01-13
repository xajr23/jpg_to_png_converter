from PIL import Image, ImageFilter

img = Image.open("Pokedex/pikachu.jpg")
#filtered_image = img.filter(ImageFilter.BLUR) #hace borrosa la imagen
#filtered_image = img.filter(ImageFilter.SMOOTH) #hace que deje de estar borrosa
#filtered_image = img.filter(ImageFilter.SHARPEN) 

filtered_image = img.convert("L") #podemos cambiar el formato de la imagen (en este caso a blanco y negro)

box = (100, 100, 400, 400)
region = filtered_image.crop(box) #corta los pixeles que pongamos en boz
#crooked_img = filtered_image.rotate(90) #rota la imagen
#resize = filtered_image.resize((640, 640))

region.save("grey.png", "png") #lo convertimos en png porque admite el .filter, con un jpg da error
#filtered_image.show() #muestra la imagen


#información de la imagen
#print(img.format)
#print(img.size)
#print(img.mode)