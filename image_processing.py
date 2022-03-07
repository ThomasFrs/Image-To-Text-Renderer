from posixpath import split
from tkinter.filedialog import askopenfilename
from PIL import Image as im
from tkinter import *
from pathlib import Path
import os

def image_opening():
  image_name = askopenfilename()
  image_file = im.open(image_name)
  return image_file, image_name

def image_resizing(width_size, image_file):
  # resize width and height to width_size
  wpercent = (width_size/float(image_file.size[0]))
  hsize = int((float(image_file.size[1])*float(wpercent)))
  image_file = image_file.resize((width_size,hsize), im.ANTIALIAS)
  # get new width and height
  width, height = image_file.size
  print("Width : {}, Height: {}".format(width, height))
  return image_file, width, height

def dark_percentage(rgb):
  if isinstance(rgb, int):
    return 100 - rgb
  return 100 - (int((((rgb[0] + rgb[1] + rgb[2])/3)*100)/255))

def pixel_to_text(image_file, image_width, image_height):
  # get each pixels
  pixel = image_file.load()
  image_list = []
  line_list = []
  shade_list = [10, 15, 20, 30, 40, 50, 60, 70, 80, 100]
  shade_value_list = ["0", "6", "3", "7", "1", "|", ";", ",", ".", " "]

  # turn each pixel into a character
  for i in range(int(image_height)):
    for j in range(int(image_width)):
      # tests which shade the pixel belongs to
      for k in range(len(shade_list)):
        if dark_percentage(pixel[j,i]) <= shade_list[k]:
          line_list.append(str(shade_value_list[k])+" "*int(round((image_width+1)/100)))
          break
    image_list.append("".join(line_list))
    line_list = []
  return image_list

def image_to_text_writing(image_list, image_name):
  file_name = ((os.path.basename(image_name)).split("."))[0]
  half_path_name = str(Path(__file__).parent.resolve()) + "/image_to_text_files"
  full_path_name = half_path_name + "/" + file_name + ".txt"
  print(full_path_name)
  # resets the file or create it if it doesn't exist
  with open(full_path_name, "w") as file:
    file.write("")
  # creates the text image
  with open(full_path_name, "a") as file:
    for line in image_list:
      file.write(line+"\n")
  #with open("image_to_text.txt", "r") as file:
    #print(file.read())

image_file, image_name = image_opening()
image_file, width, height = image_resizing(100, image_file)
image_list = pixel_to_text(image_file, width, height)
image_to_text_writing(image_list, image_name)
print(((os.path.basename(image_name)).split("."))[0])