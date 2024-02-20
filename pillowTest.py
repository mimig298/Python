from PIL import Image

with Image.open("C:/Users/migue/Downloads/miner2.png") as im:
    im = im.convert("RGBA")

r, g, b, a = im.split()
im = Image.merge("RGB", (r, g, b))