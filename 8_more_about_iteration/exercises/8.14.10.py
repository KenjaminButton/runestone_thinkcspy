'''
Sepia Tone images are those brownish colored images that may remind you of times past. The formula for creating a sepia tone is as follows:

    newR = (R × 0.393 + G × 0.769 + B × 0.189)
    newG = (R × 0.349 + G × 0.686 + B × 0.168)
    newB = (R × 0.272 + G × 0.534 + B × 0.131)

Write a function to convert an image to sepia tone. Hint: Remember that rgb values must be integers between 0 and 255.

'''

# Sepia Tone


import cImage as image

img = image.Image("elmo.gif")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        R = p.getRed()
        G = p.getGreen()
        B = p.getBlue()

        newred = int((R*0.393 + G*0.769 + B*0.189))
        newgreen = int((R*0.349 + G*0.686 + B*0.168))
        newblue = int((R*0.272 + G*0.534 + B*0.131))

        newpixel = image.Pixel(newred, newgreen, newblue)

        newimg.setPixel(col, row, newpixel)


newimg.draw(win)
win.exitonclick()
