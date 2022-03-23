from image_processing import *

def exec():
  image_file, image_name, width, height = image_opening()
  image_file, width, height = image_resizing(100, image_file)
  image_list = pixel_to_text(image_file, width, height)
  image_to_text_writing(image_list, image_name)

exec()