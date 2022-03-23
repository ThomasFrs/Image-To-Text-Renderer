from tkinter.filedialog import askopenfilename
from PIL import Image as im
from tkinter import *
from pathlib import Path
import os

def image_opening():
  """
  returns: the opened image and its path
  """
  image_name = askopenfilename()
  image_file = im.open(image_name)
  width, height = image_file.size
  return image_file, image_name, width, height

def image_resizing(width_size, image_file):
  """
  width_size: number of pixels to resize the image
  image_file: the opened image
  returns: resized image_file, its new width and height
  """
  # resize width and height to width_size
  wpercent = (width_size/float(image_file.size[0]))
  hsize = int((float(image_file.size[1])*float(wpercent)))
  image_file = image_file.resize((width_size,hsize), im.ANTIALIAS)
  # get new width and height
  width, height = image_file.size
  #print("Width : {}, Height: {}".format(width, height))
  return image_file, width, height

def black_percentage(rgb):
  """
  rgb: rgb tuple of a pixel
  returns: pixel percentage of black
  """
  if isinstance(rgb, int):
    return 100 - rgb
  return 100 - (int((((rgb[0] + rgb[1] + rgb[2])/3)*100)/255))

def pixel_to_text(image_file, image_width, image_height):
  """
  image_file: the opened image
  image_width: width of image_file
  image_height: height of image_file
  returns: list of every pixel converted into characters
  """
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
        if black_percentage(pixel[j,i]) <= shade_list[k]:
          line_list.append(str(shade_value_list[k])+" "*int(round((image_width+1)/100)))
          break
    image_list.append("".join(line_list))
    line_list = []
  return image_list

def image_to_text_writing(image_list, image_name, *args):
  """
  image_list: list of every pixel of the image converted into characters
  image_name: name of the image excluding the path
  returns: .txt file named after image_name, containing image_list
  """
  file_name = ((os.path.basename(image_name)).split("."))[0]
  half_path_name = str(Path(__file__).parent.resolve()) + "/image_to_text_files"
  full_path_name = half_path_name + "/" + file_name + ".txt"
  # resets the file or create it if it doesn't exist
  with open(full_path_name, "w") as file:
    file.write("")
  # writes the text file
  with open(full_path_name, "a") as file:
    for line in image_list:
      file.write(line+"\n")
  # prints in terminal
  if "-terminal" in args:
    with open(full_path_name, "r") as file:
      print(file.read())

def get_folder_name():
  return str(Path(__file__).parent.resolve()) + "/image_to_text_files"