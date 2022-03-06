from tkinter.filedialog import askopenfilename
from PIL import Image as im
from tkinter import *

def dark_percentage(rgb):
  return 100 - (int((((rgb[0] + rgb[1] + rgb[2])/3)*100)/255))

basewidth = 75

image = askopenfilename()
image_file = im.open(image)

wpercent = (basewidth/float(image_file.size[0]))
hsize = int((float(image_file.size[1])*float(wpercent)))
image_file = image_file.resize((basewidth,hsize), im.ANTIALIAS)
image_file.show()
pixel = image_file.load()

width, height = image_file.size
print("Width : {}, Height: {}".format(width, height))

values_list = []
shade_list = [10, 20, 30, 40, 50, 60, 100]
shade_value_list = ["3", "7", "1", "|", ",", ".", " "]

for i in range(int(height)):
  values_list = []
  for j in range(int(width)):
    for k in range(len(shade_list)):
      if dark_percentage(pixel[j,i]) <= shade_list[k]:
        values_list.append(str(shade_value_list[k])+" ")
        break

  print("".join(values_list))