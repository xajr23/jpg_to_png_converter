import sys
import os
from PIL import Image

#grab first and second argument
JPG_folder = sys.argv[1]
PNG_folder = sys.argv[2]

#check if /new exists, if not create it
if not os.path.exists(PNG_folder):
    os.makedirs(PNG_folder)

#loop through Pokedex
for file_name in os.listdir(JPG_folder):
    if file_name.endswith(".jpg"):
        img_path = os.path.join(JPG_folder, file_name)
        img = Image.open(img_path)
        clean_name = os.path.splitext(file_name)[0]

        #convert images to png
        png_path = os.path.join(PNG_folder, clean_name + ".png")
        
        #save to new folder
        img.save(png_path, "PNG")