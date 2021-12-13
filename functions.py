import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageTk
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
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
        value_names = []
        value_names.append(msg)
    return value_names
#local function for resizing image to fit preview (not used to actually resize image)
def resize_image(img):
    width = int(img.size[0])
    height = int(img.size[1])
    ratio = height/width
    height = 150
    width = int(height/ratio)
    img = img.resize((width,height))
    return img
#function for openning csv
def open_csv(root):
    global read_csv_file
    csv_file_open = filedialog.askopenfile(mode='r',title='Choose a file')
    if not csv_file_open.name.endswith(".csv"):
        return
    try:
        read_csv_file = pd.read_csv(csv_file_open)
    except ValueError:
        return
    columns = []
    csv_string = "Values: "
    for col in read_csv_file.columns:
        columns.append(col)
        csv_string += col + " "
    csv_text_available_values = Label(root,text=csv_string)
    csv_text_available_values.grid(column = 2, row = 19)


#NAMETAG FUNCTIONS
def nt_save_as_pdf(message,y,font,font_size,font_color):
    msg = message
    c = canvas.Canvas('test.pdf',pagesize=A4)
    using_csv = True
    test_array = []
    def image_to_byte_array(image:Image):
      image_byte_array = BytesIO()
      image.save(image_byte_array, format='PNG')
      image_byte_array = image_byte_array.getvalue()
      result_image = ImageReader(BytesIO(image_byte_array))
      return result_image

    temp_font_string = font+".ttf"
    myFont = ImageFont.truetype(temp_font_string, int(font_size))

    def clear_canvas():
        I1.rectangle((100, 100, 300, 150))


    while using_csv == True:
        if "<" not in message or ">" not in message:
            using_csv = False
        user_input_values = extract_input(message)
        total_array = []
        global read_csv_file
        try:
            test_array.append(read_csv_file[user_input_values].values)
        except KeyError:
            using_csv = False
            break
        except NameError:
            using_csv = False
            break
        total_array.append(read_csv_file[user_input_values].values)
        print(total_array)
        for values_index in range(len(total_array[0])):
            current_text = ""
            try:
                img = Image.open(fname)
            except NameError:
                return
            img = img.resize((248,150))
            I1 = ImageDraw.Draw(img)
            for i in range(len(total_array[0][values_index])):
                current_text += total_array[0][values_index][i] + " "
            w,h = myFont.getsize(current_text)
            I1.text(((248-w)/2,y-10), current_text , font = myFont, fill=font_color)
            finalImage = image_to_byte_array(img)
            nametag_width = 248
            nametag_height = 150
            if (values_index %10 == 0):
                c.drawImage(finalImage, 50, 30,  nametag_width, nametag_height) #x,y and w,h
                clear_canvas()
            if (values_index %10 == 1):
                c.drawImage(finalImage, 50+nametag_width+1, 30,  nametag_width, nametag_height)
                clear_canvas()
            if (values_index %10 == 2):
                c.drawImage(finalImage, 50, 30+nametag_height+2, nametag_width, nametag_height)
                clear_canvas()
            if (values_index %10 == 3):
                c.drawImage(finalImage, 50+nametag_width+1, 30+nametag_height+2,  nametag_width, nametag_height)
                clear_canvas()
            if (values_index %10 == 4):
                c.drawImage(finalImage, 50, 30+2*nametag_height+4,  nametag_width, nametag_height)
                clear_canvas()
            if (values_index %10 == 5):
                c.drawImage(finalImage, 50+nametag_width+1, 30+2*nametag_height+4,  nametag_width, nametag_height)
                clear_canvas()
            if (values_index %10 == 6):
                c.drawImage(finalImage, 50, 30+3*nametag_height+6,  nametag_width, nametag_height)
                clear_canvas()
            if (values_index %10 == 7):
                c.drawImage(finalImage, 50+nametag_width+1, 30+3*nametag_height+6,  nametag_width, nametag_height)
                clear_canvas()
            if (values_index %10 == 8):
                c.drawImage(finalImage, 50, 30+4*nametag_height+8,  nametag_width, nametag_height)
                clear_canvas()
            if (values_index %10 == 9):
                c.drawImage(finalImage, 50+nametag_width+1, 30+4*nametag_height+8,  nametag_width, nametag_height)
                clear_canvas()
                c.showPage()
        break
    if using_csv == False:
        total_array = []
        total_array.append(message)
        current_text = ""
        try:
            img = Image.open(fname)
        except NameError:
            return
        img = img.resize((248,150))
        I1 = ImageDraw.Draw(img)
        current_text = total_array[0]
        w,h = myFont.getsize(current_text)
        I1.text(((248-w)/2,y-10), current_text , font = myFont, fill=font_color)
        finalImage = image_to_byte_array(img)
        c.drawImage(finalImage, 50, 30,  248, 150) #x,y and w,h
    c.save()
def nt_open_imagefile(display,message,y,font,font_size,font_color):
    global canvas_img
    global fname
    global canvas_img_postscript
    currdir = os.getcwd()
    try:
        temp_fname = filedialog.askopenfile(mode='rb',title='Choose a file')
        img = Image.open(temp_fname)
    except AttributeError:
        return
    except OSError:
        return
    fname = temp_fname
    img = resize_image(img)
    canvas_img = ImageTk.PhotoImage(img)
    canvas = Canvas(display,width=300,height=185)
    canvas.grid(column = 2, row=1)
    canvas.create_image(0,0,image=canvas_img,anchor='nw')
    tempFont = Font(family=font, size=font_size)
    canvas.create_text(130,y,fill=font_color,font=tempFont,
    text=message)
def nt_update_preview(display,message,y,font,font_size,font_color):
    canvas = Canvas(display,width=300,height=185)
    canvas.grid(column = 2, row=1)
    try:
        canvas.create_image(0,0,image=canvas_img,anchor='nw')
    except NameError:
        return
    tempFont = Font(family=font, size=font_size)
    canvas.create_text(130,y,fill=font_color,font=tempFont,
    text=message)


#LABEL FUNCTIONS
def lbl_save_as_pdf(message,school):
    msg = message
    sch = school
    using_csv_message = True
    using_csv_school = True
    test_array = []
    c = canvas.Canvas('test.pdf',pagesize=A4)
    def image_to_byte_array(image:Image):
      image_byte_array = BytesIO()
      image.save(image_byte_array, format='PNG')
      image_byte_array = image_byte_array.getvalue()
      result_image = ImageReader(BytesIO(image_byte_array))
      return result_image

    myFont = ImageFont.truetype(r'/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf', 30)

    def clear_canvas():
        I1.rectangle((100, 100, 300, 150))

    if "<" not in msg or ">" not in msg:
        using_csv_message = False

    if  "<" not in sch or ">" not in sch:
        using_csv_school = False

    user_input_values = extract_input(message)
    school_input_values = extract_input(school)

    try:
        test_array.append(read_csv_file[user_input_values].values)
    except KeyError:
        using_csv_message = False
    except NameError:
        using_csv_message = False

    try:
        test_array.append(read_csv_file[school_input_values].values)
    except KeyError:
        using_csv_school = False
    except NameError:
        using_csv_school = False

    if using_csv_message == True:
        if using_csv_school == True:
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
            try:
                img = Image.open(fname)
            except NameError:
                return
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
        try:
            img = Image.open(fname)
        except NameError:
            return
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
    try:
        temp_fname = filedialog.askopenfile(mode='rb',title='Choose a file')
        img = Image.open(temp_fname)
    except AttributeError:
        return
    except OSError:
        return
    fname = temp_fname
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
def ctf_save_as_pdf(message,x,y,font,font_size,font_color):
    msg = message
    c = canvas.Canvas('test.pdf', pagesize=A4)
    test_array = []
    using_csv = True
    def image_to_byte_array(image:Image):
      image_byte_array = BytesIO()
      image.save(image_byte_array, format='PNG')
      image_byte_array = image_byte_array.getvalue()
      result_image = ImageReader(BytesIO(image_byte_array))
      return result_image

    temp_font_size = int(font_size)*4
    temp_font_string = font+".ttf"
    myFont = ImageFont.truetype(temp_font_string, int(temp_font_size))

    def clear_canvas():
        I1.rectangle((300, 300, 300, 300))

    while using_csv == True:
        if "<" not in message or ">" not in message:
            using_csv = False
        user_input_values = extract_input(message)
        total_array = []
        global read_csv_file
        try:
            test_array.append(read_csv_file[user_input_values].values)
        except KeyError:
            using_csv = False
            break
        except NameError:
            using_csv = False
            break
        x = x*4
        y = y*4
        total_array.append(read_csv_file[user_input_values].values)
        for values_index in range(len(total_array[0])):
            current_text = ""
            try:
                img = Image.open(fname)
            except NameError:
                return
            img = img.resize((848,600))
            I1 = ImageDraw.Draw(img)
            for i in range(len(total_array[0][values_index])):
                current_text += total_array[0][values_index][i] + " "
            w,h = myFont.getsize(current_text)
            I1.text((x-w/2,y-20), current_text , font = myFont, fill=font_color)
            finalImage = image_to_byte_array(img)
            c.translate(A4[0]/2, A4[1]/2)
            c.rotate(90)
            c.drawImage(finalImage, -425, -300,  848, 600) #x,y and w,h
            clear_canvas()
            c.showPage()
        break
    if using_csv == False:
        total_array = []
        total_array.append(message)
        current_text = ""
        try:
            img = Image.open(fname)
        except NameError:
            return
        img = img.resize((848,600))
        I1 = ImageDraw.Draw(img)
        current_text = total_array[0]
        w,h = myFont.getsize(current_text)
        x = x*4
        y = y*4
        I1.text((x-w/3,y-20), current_text , font = myFont, fill=font_color)
        finalImage = image_to_byte_array(img)
        c.translate(A4[0]/2, A4[1]/2)
        c.rotate(90)
        c.drawImage(finalImage, -425, -300,  848, 600) #x,y and w,h
        clear_canvas()
    c.save()
def ctf_open_imagefile(display,message,x,y,font,font_size,font_color):
    global canvas_img
    global fname
    currdir = os.getcwd()
    try:
        temp_fname = filedialog.askopenfile(mode='rb',title='Choose a file')
        img = Image.open(temp_fname)
    except AttributeError:
        return
    except OSError:
        return
    fname = temp_fname
    img = resize_image(img)
    canvas_img = ImageTk.PhotoImage(img)
    canvas = Canvas(display,width=250,height=185)
    canvas.grid(column = 2, row=1)
    canvas.create_image(0,0,image=canvas_img,anchor='nw')
    tempFont = Font(family=font, size=font_size)
    canvas.create_text(x,y,fill=font_color,font=tempFont,
    text=message)
def ctf_update_preview(display,message,x,y,font,font_size,font_color):
    canvas = Canvas(display,width=300,height=185)
    canvas.grid(column = 2, row=1)
    try:
        canvas.create_image(0,0,image=canvas_img,anchor='nw')
    except NameError:
        return
    tempFont = Font(family=font, size=font_size)
    canvas.create_text(x,y,fill=font_color,font=tempFont,
    text=message)
