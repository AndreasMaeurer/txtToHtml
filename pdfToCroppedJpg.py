# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 13:34:43 2022
@author: andreas

Notes:
    qwenview shows W x H

References:
    https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/
    https://pdf2image.readthedocs.io/en/latest/installation.html
    https://stackoverflow.com/questions/9983263/how-to-crop-an-image-using-pil
    https://www.geeksforgeeks.org/python-pil-image-save-method/
"""

"""-------------------------------------------------------------------------"""
"""---Get Pdf and convert to Jpeg-------------------------------------------"""
# import module
from pdf2image import convert_from_path

# Store Pdf with convert_from_path function
images = convert_from_path('example.pdf')

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')

"""-------------------------------------------------------------------------"""
"""---Crop Image.  Basically remove the margins-----------------------------"""
from PIL import Image
img = Image.open("page0.jpg")
#area = (200, 200, 400, 400)
#cropped_img = img.crop(area)
#cropped_img.show()

from PIL import ImageOps

border = (135, 150, 320, 160) # left, top, right, bottom
croppedImg = ImageOps.crop(img, border)
croppedImg.show()
im2 = croppedImg.save("printThisCroppedImage.jpg")

"""-------------------------------------------------------------------------"""
"""---Split Image ----------------------------------------------------------"""
#(left, upper, right, lower)
#from PIL import Image
img3 = Image.open("printThisCroppedImage.jpg")

#the example image is 800 x 600
#my image is 1245 x 1891
"""
img_left_area = (0, 0, 400, 600)
img_right_area = (400, 0, 800, 600)
img_top_area = (0, 0, 800, 300)
img_bottom_area = (0, 300, 800, 600)
"""

img_top_area = (0, 0, 1245, 946)
img_bottom_area = (0, 946, 1245, 1891)

"""
img_left = img.crop(img_left_area)
img_right = img.crop(img_right_area)

img_left.show()
img_right.show()
"""

img_top = img3.crop(img_top_area)
img_bottom = img3.crop(img_bottom_area)

img_top.show()
img_bottom.show()

fim1 = img_top.save("fim1.jpg")
fim2 = img_bottom.save("fim2.jpg")
