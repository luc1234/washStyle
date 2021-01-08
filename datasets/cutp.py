import os
from PIL import Image

p = '/home/luc/hhh/'
a = os.listdir(p)

for i in a:
	path = p+i
        print path
        try:
            f = Image.open(path)
        except:

            continue

        else:
            xsize,ysize=f.size
            box=(180,185,xsize-225,ysize-110)
            f.crop(box).save(path)
