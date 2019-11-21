# #缩放
# from PIL import Image
# im = Image.open('test.jpg')
# w,h =im.size
# print('Original image size:%sx%s'%(w,h))
# im.thumbnail((w//2,h//2))
# print('Resize image to:%sx%s'%(w//2,h//2))
# im.save('thumbnail.jpg','jpeg')

# #模糊
# from PIL import Image,ImageFilter
# im = Image.open('test.jpg')
# im2 =im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg','jpeg')

from PIL import Image,ImageFilter,ImageFont,ImageDraw	
import random

#随机字母
def rndChar():
	return chr(random.randint(65,90))

#随机颜色1
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
#创建image对象
w = 60*4
h = 60
image = Image.new('RGB', (w,h),(255,255,255))
#创建Font对象
Font = ImageFont.truetype('arial.ttf',36)
#创建Draw对象
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(w):
	for y in range (h):
		draw.point((x,y),fill = rndColor())
#输出文字
for t in range(4):
	draw.text((60 * t + 10,10),rndChar(),font=Font,fill=rndColor2())

#模糊：
im = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')



