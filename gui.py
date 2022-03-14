from cgitb import text
from tkinter import *
from webbrowser import get
from image_processing import *

class GUI(Frame):
  def __init__(self):
    self.window_width = 1280
    self.window_height = 720

    Frame.__init__(self)
    self.grid()
    self.master.title("Image To Text Renderer")
    self.master.geometry("{}x{}".format(self.window_width,self.window_height))
    self.master.resizable(0,0)

    self.main_frame = Frame(self, width=self.window_width, height=self.window_height)
    self.main_frame.grid_propagate(0)
    self.main_frame.grid()

    self.resize_input_box()
    self.frames_layout()
    self.header_layout()
    self.mainloop()

  def image_processing(self):
    image_file, image_name, self.image_width, self.image_height = image_opening()
    image_file, width, height = image_resizing(100, image_file)
    image_list = pixel_to_text(image_file, width, height)
    image_to_text_writing(image_list, image_name)

  def resize_input_box(self):
    self.desired_width_entry = IntVar()

    self.resize_box = Tk()
    self.resize_box.geometry("{}x{}+{}+{}".format(400, 200, int(self.master.winfo_screenwidth()/2), int(self.master.winfo_screenheight()/2)))
    current_width = Label(self.resize_box, text="Current width : ",  font=(20))
    current_width.grid()
    current_height = Label(self.resize_box, text="Current height : ",  font=(20))
    current_height.grid()
    desired_width = Label(self.resize_box, text="Desired width : ",  font=(20))
    desired_width.grid()
    input_width = Entry(self.resize_box, textvariable=self.desired_width_entry, font=(20))
    input_width.grid()
    input_button = Button(self.resize_box, text="Confirm", command=self.return_new_width, font=(20))
    input_button.grid()

  def return_new_width(self):
    return self.desired_width_entry.get()

  def frames_layout(self):
    self.header = Frame(self.main_frame, width=self.window_width, height=self.window_height/20, bg="gold")
    self.header.grid(row=0, column=0, sticky=NW)
    self.header.grid_propagate(0)

    self.file_list = Frame(self.main_frame, width=self.window_width/5, height=19*self.window_height/20, bg="red")
    self.file_list.grid(row=1, column=0, sticky=W)
    self.file_list.grid_propagate(0)

    self.text_image_display = Frame(self.main_frame, width=4*self.window_width/5, height=19*self.window_height/20, bg="green")
    self.text_image_display.grid(row=1, column=0, sticky=E)
    self.text_image_display.grid_propagate(0)

  def header_layout(self):
    self.import_frame = Frame(self.header, width=self.window_width/10, height=self.window_height/20, bg="blue")
    self.import_frame.grid()
    import_text = Button(self.import_frame, text="Import", command=self.image_processing, font=(8))
    import_text.grid()

    self.theme_frame = Frame(self.header, width=self.window_width/10, height=self.window_height/20, bg="blue")
    self.theme_frame.grid()
    import_text = Button(self.import_frame, text="Theme", font=(8))
    import_text.grid(row=0, column=1)

gui = GUI()