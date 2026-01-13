from PIL import Image, ImageFilter

img = Image.open("astro.jpg")

#si hacemos esto la imagen puede quedar aplastada
# new_img = img.resize((400,200))
# new_img.save("thumbnail.jpg")

#para hacer que la imagen mantenga la relación de aspecto podemos hacer esto:
img.thumbnail((400, 200))
img.save("thumbnail.jpg")

