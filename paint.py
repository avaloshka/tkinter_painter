# For Windows 10 users I would import next 2 lines to capture the display at always 100%- no zoom in, otherwise please make sure your screen settings set at display 100%
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)

from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageGrab, ImageTk
import PIL
from tkinter import messagebox


root = Tk()
root.title('Painter')
root.geometry("800x800")

brush_color = 'black'


# Change the size of the brush
def paint(e): # e is event

	# Brush Parameters
	brush_width = int(my_slider.get())
	
	# Brush type: BUTT, ROUND, PROJECTING
	brush_type2 = brush_type.get() # Needed to change variable- otherwise it was called before it was assigned

	# starting position
	x1 = e.x - 1
	y1 = e.y - 1
	# ending position
	x2 = e.x + 1
	y2 = e.y + 1
	# draw on the canvas
	my_canvas.create_line(x1, y1, x2, y2, fill=brush_color,
	 width=brush_width,
	 capstyle=brush_type2,
	  smooth=True)

def change_brush_size(thing): # thing or e is needed to get slider text updated
	slider_label.config(text=int(my_slider.get())) 


def change_brush_color():
	global brush_color 
	brush_color = 'black'
	brush_color = colorchooser.askcolor(color=brush_color)[1]
	

def change_canvas_color():
	global bg_color
	bg_color = 'black'
	bg_color = colorchooser.askcolor(color=bg_color)[1]
	my_canvas.config(bg=bg_color)

def clear_screen():
	my_canvas.delete("all")
	my_canvas.config(bg='white')

def save_as_png():
	# result - is the place where the file will be saved
	result = filedialog.asksaveasfilename(
		initialdir='c:/Users/alexv/Desktop/paint',
		filetypes=(("png files", "*.png"), ("all files", "*.*"))
		)

	if result.endswith('.png'):
		pass
	# These make extention .png
	else:
		result = result + '.png'
	if result:
		x = root.winfo_rootx() + my_canvas.winfo_x()
		y = root.winfo_rooty() + my_canvas.winfo_y()
		x1 = x + my_canvas.winfo_width()
		y1 = y + my_canvas.winfo_height()
		# ImageGrab.grab().crop((425,701,23,98)).save(result)
		ImageGrab.grab().crop((x, y , x1, y1)).save(result)

		# Pop up Success message
		messagebox.showinfo("Image saved", "Your image has been saved!")



# Create our canvas
w = 600
h = 400
my_canvas = Canvas(root, width=w, height=h, bg='white')
my_canvas.pack(pady=20)
my_canvas.bind('<B1-Motion>', paint)

# Create First Frame

# Create Brush Options Frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

# Brush Size Frame
brush_size_frame = LabelFrame(brush_options_frame, text='Brush Size')
brush_size_frame.grid(row=0, column=0, padx=50)
# Brush Slider
my_slider = ttk.Scale(brush_size_frame, from_=1, to=100,
 command=change_brush_size,
  orient=VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)

# Brush Slider Label (to reflect the changing units)
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)

# Now Create Second Frame

# Brush Type
brush_type_frame = LabelFrame(brush_options_frame, text='Brush Type',
	height=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set("round")

# Create Radio Buttons for Brush Type
brush_type_radio1 = Radiobutton(brush_type_frame, text='Round',
	variable=brush_type, value='round')
brush_type_radio2 = Radiobutton(brush_type_frame, text='Slash',
	variable=brush_type, value='butt')
brush_type_radio3 = Radiobutton(brush_type_frame, text='Diamond',
	variable=brush_type, value='projecting')

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# Change Colors
change_colors_frame = LabelFrame(brush_options_frame, text='Change Colors')
change_colors_frame.grid(row=0, column=2)

# Change Brush Color Button
brush_color_button = Button(change_colors_frame, text='Brush color',
	command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)

# Change Canvas Background Color
canvas_color_button = Button(change_colors_frame, text='Canvas Color',
	command=change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)

# Program Options Frame
options_frame = LabelFrame(brush_options_frame, text='Program Options')
options_frame.grid(row=0, column=3, padx=50)

# Clear Screen Button
clear_button = Button(options_frame, text='Clear Screen', command=clear_screen)
clear_button.pack(padx=10, pady=10)

# Save Image
save_image_button = Button(options_frame, text='Save to PNG', command=save_as_png)
save_image_button.pack(pady=10, padx=10)


root.mainloop()
