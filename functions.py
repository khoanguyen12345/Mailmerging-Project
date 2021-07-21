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
import pandas as pd

global fname
global read_csv_file

def extract_input(message):
    msg = message
    if "<" in msg:
        start = "<"
        end = ">"
        value_names = msg.split(">")
        value_names.pop()
        for i in range(len(value_names)):
            if value_names[i].startswith(" "):
                value_names[i] = value_names[i][1:]
            value_names[i] = value_names[i].replace("<", "")
    else:
        value_names.append(msg)
    return value_names

def open_csv(root):
    global read_csv_file
    csv = filedialog.askopenfile(mode='r',title='Choose a file')
    column_names = []
    csv_string = "Available values: "
    read_csv_file = pd.read_csv(csv)
    for col_name in read_csv_file.columns:
        column_names.append(col_name)
        csv_string += col_name + " "
    csv_text = Label(root,text=csv_string)
    csv_text.grid(column = 2, row = 7)

def save_as_pdf(message,x,y):
    msg = message
    c = canvas.Canvas('test.pdf')

    def image_to_byte_array(image:Image):
      imgByteArr = BytesIO()
      image.save(imgByteArr, format=image.format)
      imgByteArr = imgByteArr.getvalue()
      final = ImageReader(BytesIO(imgByteArr))
      return final

    myFont = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\timesbd.ttf', 100)

    def clear_canvas():
        I1.rectangle((100, 100, 300, 150))

    if "<" in msg:
        user_input_values = extract_input(message)
        total_array = []
        global read_csv_file
        total_array.append(read_csv_file[user_input_values].values)
        print(total_array)
        for values_index in range(len(total_array[0])):
            current_text = ""
            img = Image.open(fname)
            I1 = ImageDraw.Draw(img)
            W = int(img.size[0])
            H = int(img.size[1])
            ratio = H/W
            nametag_height = 150
            nametag_width = int(nametag_height/ratio)
            for i in range(len(total_array[0][values_index])):
                current_text += total_array[0][values_index][i] + " "
            w,h = myFont.getsize(current_text)

            I1.text(((W-w)/2,(H-h)/2-(185-y)*(150/185)), current_text , font = myFont, fill="black")
            finalImage = image_to_byte_array(img)

            if (values_index %6 == 0):
                c.drawImage(finalImage, 50, 30,  nametag_width, nametag_height) #x,y and w,h
                clear_canvas()
            if (values_index %6 == 1):
                c.drawImage(finalImage, 50+nametag_width+10, 30,  nametag_width, nametag_height)
                clear_canvas()
            if (values_index %6 == 2):
                c.drawImage(finalImage, 50, 30+nametag_height+10, nametag_width, nametag_height)
                clear_canvas()
            if (values_index %6 == 3):
                c.drawImage(finalImage, 50+nametag_width+10, 30+nametag_height+10,  nametag_width, nametag_height)
                clear_canvas()
            if (values_index %6 == 4):
                c.drawImage(finalImage, 50, 30+2*nametag_height+20,  nametag_width, nametag_height)
                clear_canvas()
            if (values_index %6 == 5):
                c.drawImage(finalImage, 50+nametag_width+10, 30+2*nametag_height+20,  nametag_width, nametag_height)
                clear_canvas()
                c.showPage()

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
