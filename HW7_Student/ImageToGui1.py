
from PIL import Image,ImageTk
from tkinter import *
from tkinter import filedialog

import os

from PIL import ImageTk

ASCII_CHARS = ['#', 'M', '8', 'L', '/', 'i', ':', '>', '.', '`', ' ']
root = Tk()
currdir = os.getcwd()
tempdir = ''
width = 500
contrast = 1
bright = 1
color = 1
sharp = 1


def browse():
    currdir = os.getcwd()
    global tempdir
    tempdir = filedialog.askopenfilename(filetypes=(("All files", "*.*"), ("png", "*.png")))



# def scale_image(image, new_width=100):
#     print (new_width)

#     """Resizes an image preserving the aspect ratio.
#     """
#     (original_width, original_height) = image.size
#     aspect_ratio = original_height/float(original_width)*0.6
#     new_height = int(aspect_ratio * new_width)

#     new_image = image.resize((new_width, new_height))
#     return new_image

# def convert_to_grayscale(image):
#     return image.convert('L')

# def map_pixels_to_ascii_chars(image, range_width=25):
#     """Maps each pixel to an ascii char based on the range
#     in which it lies.

#     0-255 is divided into 11 ranges of 25 pixels each.
#     """

#     pixels_in_image = list(image.getdata())
#     pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
#             pixels_in_image]

#     return "".join(pixels_to_chars)

# def convert_image_to_ascii(image, new_width=100):
#     image = scale_image(image, new_width)
#     image = convert_to_grayscale(image)

#     pixels_to_chars = map_pixels_to_ascii_chars(image)
#     len_pixels_to_chars = len(pixels_to_chars)

#     image_ascii = [pixels_to_chars[index: index + new_width] for index in
#             range(0, len_pixels_to_chars, new_width)]

#     return "\n".join(image_ascii)

# def handle_image_conversion(image_filepath, new_width):
#     image = None
#     try:
#         image = Image.open(image_filepath)
#     except Exception (e):
#         print ("Unable to open image file {image_filepath}.".format(image_filepath=image_filepath))
#         print (e)
#         return

#     image_ascii = convert_image_to_ascii(image, new_width)
#     print (image_ascii)
def twitch():
    global width
    width = "twitch"
    print(width)
def youtube():
    global width
    width = 56
def enter(e):
    v= e.get().split(',')
    try:
        global contrast
        contrast=float(v[0])
        global bright
        bright =float(v[1])
        global color
        color = float(v[2])
        global sharp
        sharp = float(v[3])
    except:
        pass
def start(f):
    from ImageToAscii1 import handle_image_conversion
    from ImageToAscii1 import get_enhance_iamge
    handle_image_conversion(tempdir, width, contrast, bright, color, sharp)
    # photo = PhotoImage(file = "img.png")
    # panel = Label(f, image = photo)
    # panel.image = photo

	# image_file_path = tempdir
    # #image_width = sys.argv[2]
    # new_width = 
    # aspect_ratio = float(sys.argv[3])
    # print (new_width)

    # handle_image_conversion(image_file_path, new_width)

if __name__=='__main__':
    import sys


    root.title("emote")
    root.geometry("500x400")

    frame = Frame(root)
    frame.pack()

    imageLabel = Label(frame, text='Select your image').pack(side = LEFT)
    buttonUpload = Button(frame, text='Browse', command = browse)

    buttonYoutube = Button(frame, text='Youtube', command=youtube)
    buttonTwitch = Button(frame, text='Twitch', command=twitch)
    buttonUpload.pack(side=LEFT)

    buttonTwitch.pack(side = LEFT)
    buttonYoutube.pack(side = LEFT)
    frame1 = Frame(root)
    frame1.pack(side=TOP)
    imageLabel1 = Label(frame1, text='Enter constrast,brightness,color,sharpness (All 1-3): ').pack(side=LEFT)
    e = Entry(frame1)
    buttonEnter = Button(frame1, text='Enter', command=lambda: enter(e))
    buttonEnter.pack(side = LEFT)
    e.pack(side=LEFT)
    frame2 = Frame(root)
    frame2.pack(side = LEFT)
    buttonStart = Button(frame, text='start', command=lambda:start(frame2))
    buttonStart.pack(side=LEFT)
    root.mainloop()