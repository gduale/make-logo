import Image
# p1 = Image.open('fond.png')
# p2 = Image.open('1.png')
# #p3 = Image.blend(p1, p2, .8)
# p3 = Image.new('RGBA', (512,512))
# p3.paste(p1,p2)
# p3.save('fusion.png')

background = Image.open("fond.png")
foreground = Image.open("1.png")

background.paste(foreground, (0, 0), foreground)
background.save('fusion.png')

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
img = Image.open("fusion.png")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("fonts/Infinite_Stroke.otf", 56)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((50, 50),"Sample Text",(255,255,255),font=font)
img.save('sample-out.jpg')
