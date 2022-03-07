from tkinter.filedialog import askopenfilename
from turtle import width
from PIL import Image as im
from tkinter import *

def image_opening():
  image = askopenfilename()
  image_file = im.open(image)
  image_resizing(75, image_file)

def image_resizing(width_size, image_file):
  # resize width and height to width_size
  wpercent = (width_size/float(image_file.size[0]))
  hsize = int((float(image_file.size[1])*float(wpercent)))
  image_file = image_file.resize((width_size,hsize), im.ANTIALIAS)
  # get new width and height
  width, height = image_file.size
  print("Width : {}, Height: {}".format(width, height))

  pixel_to_text(image_file, width, height)

def dark_percentage(rgb):
  return 100 - (int((((rgb[0] + rgb[1] + rgb[2])/3)*100)/255))

def pixel_to_text(image_file, image_width, image_height):
  # get each pixels
  pixel = image_file.load()
  image_list = []
  values_list = []
  shade_list = [10, 15, 20, 30, 40, 50, 60, 70, 80, 100]
  shade_value_list = ["0", "6", "3", "7", "1", "|", ";", ",", ".", " "]

  # turn each pixel into a character
  for i in range(int(image_height)):
    for j in range(int(image_width)):
      # tests which shade the pixel belongs to
      for k in range(len(shade_list)):
        if dark_percentage(pixel[j,i]) <= shade_list[k]:
          values_list.append(str(shade_value_list[k])+" "*int(round((image_width+1)/100)))
          break
    image_list.append("".join(values_list))
    values_list = []
  for elt in image_list:
    print(elt)

image_opening()