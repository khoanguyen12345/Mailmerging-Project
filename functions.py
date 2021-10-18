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

#GENERAL FUNCTIONS
#function for extracting input from Text (inside <> e.g. <first name> will extract first name)
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
#local function for resizing image to fit preview (not used to actually resize image)
def resize_image(img):
    width = int(img.size[0])
    height = int(img.size[1])
    ratio = height/width
    height = 185
    width = int(height/ratio)
    img = img.resize((width,height))
    return img
#function for openning csv
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
    csv_text.grid(column = 2, row = 8)


#NAMETAG FUNCTIONS
def nt_save_as_pdf(message,x,y):
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
    else:
        total_array = []
        total_array.append(message)

        if "<" in msg:
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
        else:
            current_text = ""
            img = Image.open(fname)
            I1 = ImageDraw.Draw(img)
            W = int(img.size[0])
            H = int(img.size[1])
            ratio = H/W
            nametag_height = 150
            nametag_width = int(nametag_height/ratio)
            current_text = total_array[0]
            w,h = myFont.getsize(current_text)
            I1.text(((W-w)/2,(H-h)/2-(185-y)*(150/185)), current_text , font = myFont, fill="black")
            finalImage = image_to_byte_array(img)
            c.drawImage(finalImage, 50, 30,  nametag_width, nametag_height) #x,y and w,h
    c.save()
def nt_open_imagefile(display,message,x,y):
    global canvas_img
    global fname
    currdir = os.getcwd()
    fname = filedialog.askopenfile(mode='rb',title='Choose a file')
    img = Image.open(fname)
    img = resize_image(img)
    canvas_img = ImageTk.PhotoImage(img)
    canvas = Canvas(display,width=300,height=185)
    canvas.grid(column = 2, row=1)
    canvas.create_image(0,0,image=canvas_img,anchor='nw')
    canvas.create_text(x,y,fill="black",font="Times 20 bold",
    text=message)

#LABEL FUNCTIONS
def lbl_save_as_pdf(message,school):
    msg = message
    sch = school
    c = canvas.Canvas('test.pdf')
    def image_to_byte_array(image:Image):
      imgByteArr = BytesIO()
      image.save(imgByteArr, format=image.format)
      imgByteArr = imgByteArr.getvalue()
      final = ImageReader(BytesIO(imgByteArr))
      return final

    myFont = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\timesbd.ttf', 30)

    def clear_canvas():
        I1.rectangle((100, 100, 300, 150))

    if "<" in msg:
        if "<" in sch:
            user_input_values = extract_input(message)
            school_input_values = extract_input(school)
            temp_name_array = []
            temp_school_array = []
            for names in read_csv_file[user_input_values].values:
                temp_name_array.append(" ".join(names))
            for schools in read_csv_file[school_input_values].values:
                temp_school_array.append(schools[0])
        else:
            user_input_values = extract_input(message)
            temp_name_array = []
            temp_school_array = []
            for names in read_csv_file[user_input_values].values:
                temp_name_array.append(" ".join(names))
                temp_school_array.append(school)
        column_temp = 0
        for values_index in range(len(temp_name_array)):
            name_text = ""
            school_text = ""
            img = Image.open(fname)
            I1 = ImageDraw.Draw(img)
            W = int(img.size[0])
            H = int(img.size[1])
            ratio = H/W
            label_height = 82
            label_width = int(label_height/ratio)
            name_text = temp_name_array[values_index]
            school_text = temp_school_array[values_index]
            w_name,h_name = myFont.getsize(name_text)
            w_school, h_school = myFont.getsize(school_text)

            I1.text(((W-w_name)/2,(H-h_name)/3), name_text , font = myFont, fill="black")
            I1.text(((W-w_school)/2,(H-h_school)/3*2), school_text, font = myFont, fill="black")

            finalImage = image_to_byte_array(img)
            if values_index % 3 == 0:
                c.drawImage(finalImage, 0, label_height*column_temp,  label_width, label_height) #x,y and w,h
                clear_canvas()
            if values_index % 3 == 1:
                c.drawImage(finalImage, label_width, label_height*column_temp,  label_width, label_height) #x,y and w,h
                clear_canvas()
            if values_index % 3 == 2:
                c.drawImage(finalImage, label_width*2, label_height*column_temp,  label_width, label_height) #x,y and w,h
                column_temp+=1
                clear_canvas()
            if values_index %3 ==2 and column_temp == 9:
                c.showPage()
                column_temp = 0
    else:
        current_text = ""
        img = Image.open(fname)
        I1 = ImageDraw.Draw(img)
        W = int(img.size[0])
        H = int(img.size[1])
        ratio = H/W
        nametag_height = 120
        nametag_width = int(nametag_height/ratio)
        current_text = message
        current_school = school
        w,h = myFont.getsize(current_text)
        I1.text(((W-w)/3,(H-h)/3), current_text , font = myFont, fill="black")
        I1.text(((W-w)/3,(H-h)/3*2), current_school, font = myFont, fill="black")
        finalImage = image_to_byte_array(img)
        c.drawImage(finalImage, 50, 30,  nametag_width, nametag_height) #x,y and w,h

    c.save()
def lbl_open_imagefile(display,message,school):
    global canvas_img
    global fname
    currdir = os.getcwd()
    fname = "localresources/label.jpg"
    img = Image.open(fname)
    img = img.resize((202,100))
    canvas_img = ImageTk.PhotoImage(img)
    canvas = Canvas(display,width=300,height=185)
    canvas.grid(column = 2, row=1)
    canvas.create_image(50,50,image=canvas_img,anchor='nw')
    canvas.create_text(155,90,fill="black",font="Times 10 bold",
    text=message)
    canvas.create_text(155,110,fill="black",font="Times 10 bold",
    text=school)

#CERTIFICATE FUNCTIONS
