from PIL import Image
import os

img = Image.open(input("What is the reference image? "))
Direc = input("From which folder do you want to make the images look like the reference? ")
files = os.listdir(Direc)
files = [f for f in files if os.path.isfile(Direc+'/'+f)]

for file_n in range(len(files)):
    file = files[file_n]
    im = Image.open(Direc + "/" + file)
    imga = img.resize(im.size)
    imga.save(Direc + "/" + file)
    print("File", file, "saved successfully! (", round(file_n*100/len(files), 2), "% complete!)")