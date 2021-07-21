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
import panda as pd

global fname
global csv

def open_csv():


def save_as_pdf(message,x,y):
    img = Image.open(fname)
    I1 = ImageDraw.Draw(img)
    W = int(img.size[0])
    H = int(img.size[1])
    ratio = H/W
    nametag_height = 150
    nametag_width = int(nametag_height/ratio)
    msg = message


    myFont = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\timesbd.ttf', 100)
    w,h = myFont.getsize(msg)

    I1.text(((W-w)/2,(H-h)/2-(185-y)*(150/185)), msg , font = myFont, fill="black")
    c = canvas.Canvas('ex1.pdf')
    def image_to_byte_array(image:Image):
      imgByteArr = BytesIO()
      image.save(imgByteArr, format=image.format)
      imgByteArr = imgByteArr.getvalue()
      final = ImageReader(BytesIO(imgByteArr))
      return final
    finalImage = image_to_byte_array(img)

    c.drawImage(finalImage, 50, 30,  nametag_width, nametag_height) #x,y and w,h
    c.drawImage(finalImage, 50+nametag_width+10, 30,  nametag_width, nametag_height)

    c.drawImage(finalImage, 50, 30+nametag_height+10, nametag_width, nametag_height)
    c.drawImage(finalImage, 50+nametag_width+10, 30+nametag_height+10,  nametag_width, nametag_height)

    c.drawImage(finalImage, 50, 30+2*nametag_height+20,  nametag_width, nametag_height)
    c.drawImage(finalImage, 50+nametag_width+10, 30+2*nametag_height+20,  nametag_width, nametag_height)

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
    canvas.create_text(x,y,fill="black",font="Times 20 bold",
                        text=message)

def resize_image(img):
    width = int(img.size[0])
    height = int(img.size[1])
    ratio = height/width
    height = 185
    width = int(height/ratio)
    img = img.resize((width,height))
    return img
