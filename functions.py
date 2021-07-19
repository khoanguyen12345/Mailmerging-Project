import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageTk
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.utils import ImageReader
from io import BytesIO

global fname

def image_to_byte_array(image:Image):
  imgByteArr = BytesIO()
  image.save(imgByteArr, format=image.format)
  imgByteArr = imgByteArr.getvalue()
  final = ImageReader(BytesIO(imgByteArr))
  return final

def save_as_pdf(message):
    img = Image.open(fname)
    I1 = ImageDraw.Draw(img)
    W = img.size[0]
    H = img.size[1]
    ratio = H/W
    msg = message
    myFont = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 300)
    w, h = myFont.getsize(msg)
    I1.text(((W-w)/2,(H-h)/2.5), msg,font = myFont, fill="black")
    c = canvas.Canvas('ex1.pdf')
    finalImage = image_to_byte_array(img)
    c.drawImage(finalImage, 0, 0,  int(6/ratio)*cm, 6*cm) #w,h
    c.drawImage(finalImage, 260, 0,  int(6/ratio)*cm, 6*cm)
    c.showPage()
    c.save()


def open_imagefile(root,message,x,y):
    global canvas_img
    global fname
    currdir = os.getcwd()
    fname = filedialog.askopenfile(mode='rb',title='Choose a file')
    img = Image.open(fname)
    img = resize_image(img)
    canvas_img = ImageTk.PhotoImage(img)
    canvas = Canvas(root,width=300,height=185)
    canvas.grid(column = 2, row=1)
    canvas.create_image(0,0,image=canvas_img,anchor='nw')
    canvas.create_text(x,y,fill="darkblue",font="Times 20 bold",
                        text=message)

def resize_image(img):
    width = int(img.size[0])
    height = int(img.size[1])
    ratio = height/width
    height = 185
    width = int(height/ratio)
    img = img.resize((width,height))
    return img
