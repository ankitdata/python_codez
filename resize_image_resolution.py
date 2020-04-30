"""
This code will help to resize the over size image to any lower resolution size
give input image path and
output image path
pip install pillow ; numpy ; python-resize-image
"""

from PIL import Image
from numpy import asarray
from resizeimage import resizeimage

image = Image.open(r'path\to\input\image\image.png')
# convert image to numpy array
data = asarray(image)
print(data)
# data type
print(type(data))
# summarize shape
print(data.shape)

from resizeimage import resizeimage

with open(r'path\to\input\image\image.png', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [1920,2944]) # change shape here
        cover.save('path/to/save/output/image.png', image.format)
