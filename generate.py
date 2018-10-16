import numpy as np
from PIL import ImageFont, ImageDraw, Image
import PIL.ImageOps

W = 200
H = 300
font = ImageFont.truetype("font/arial.ttf", int(H*8/10))

for i in range(31, 128) :
    img = Image.new('RGB', (W, H))
    draw = ImageDraw.Draw(img)
    # use a truetype font
    text = chr(i)
    # print(text)
    w, h = draw.textsize(text, font=font)
    draw.text(((W-w)/2, (H-h)/2), text, font=font)

    inverted_image = PIL.ImageOps.invert(img)
    name = str(i) + ".jpg"
    name = "image/" + name
    inverted_image.save(name)