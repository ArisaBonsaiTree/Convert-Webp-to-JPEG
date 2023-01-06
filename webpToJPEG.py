from PIL import Image
import os

directory = os.getcwd()

for filename in os.listdir(directory):
    if filename.endswith(".webp"):
        im = Image.open(filename)
        filename_without_ext = os.path.splitext(filename)[0]
        im.save(filename_without_ext, "jpeg")
        continue
    else:
        continue