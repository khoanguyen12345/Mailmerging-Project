import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageDraw
from functions import nt_save_as_pdf,nt_open_imagefile, nt_update_preview
from functions import lbl_save_as_pdf,lbl_open_imagefile
from functions import ctf_save_as_pdf,ctf_open_imagefile, ctf_update_preview
from functions import open_csv
import os


root = tk.Tk()
root.geometry('+%d+%d'%(350,10))
update_in_progress = False



#interactables frame
interactables = Frame(root,height=200,width=200)
interactables.grid(columnspan=4, rowspan=20, row=0,column=0)



#display frame
display = Frame(root,height = 200,width=200)
display.grid(columnspan = 2, rowspan = 10,row=0,column=4)

#options menu (checklist format)
options_list = ["Nametag", "Label", "Certificate"]
format_option = tk.StringVar(interactables)
format_option.set("Select an Option")
question_menu = tk.OptionMenu(interactables, format_option, *options_list)
question_menu.grid(column = 2, row = 1)

#ELEMENTS FOR NAMETAGS
#labels
nt_name_label = Label(interactables, text="Text: ", font=("Raleway", 10))
nt_y_position_label = Label(interactables, text="Text Y Position: ", font=("Raleway", 10))
nt_font_label = Label(interactables, text="Text Font: ", font=("Raleway", 10))
nt_font_size_label = Label(interactables, text="Text Font Size: ", font=("Raleway", 10))
nt_font_color_label = Label(interactables, text="Text Color: ", font=("Raleway", 10))
#text input
nt_name = tk.StringVar()
nt_nameEntered = ttk.Entry(interactables, width = 15, textvariable = nt_name)
#open csv button
nt_csv_btn = Button(interactables,text = "Open CSV", command= lambda:open_csv(interactables),font = "Arial", bg = "#20bebe",fg = "white",height = 1,width=15)
#y potition text input
nt_y_position = tk.StringVar(value = "60")
nt_y_position = ttk.Entry(interactables, width = 15, textvariable = nt_y_position)
nt_y_position.insert(END, "60")
#font text input
nt_font = tk.StringVar(value = "times")
nt_font = ttk.Entry(interactables, width = 15, textvariable = nt_font)
nt_font.insert(END, "times")
#font size text input
nt_font_size = tk.StringVar(value = "15")
nt_font_size = ttk.Entry(interactables, width = 15, textvariable = nt_font_size)
nt_font_size.insert(END, "15")
#font color text input
nt_font_color = tk.StringVar(value = "#000000")
nt_font_color = ttk.Entry(interactables, width = 15, textvariable = nt_font_color)
nt_font_color.insert(END, "#000000")
#buttons
nt_browse_btn = Button(interactables, text="Browse", command= lambda:nt_open_imagefile(display,nt_name.get(),nt_y_position.get(),nt_font.get(),nt_font_size.get(),nt_font_color.get()), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
nt_save_pdf_btn = Button(interactables,text = "Save As PDF", command= lambda:nt_save_as_pdf(nt_name.get(),int(nt_y_position.get()),nt_font.get(),nt_font_size.get(),nt_font_color.get()),font = "Arial", bg = "#20bebe",fg = "white",height = 1,width=15)
nt_update_preview_btn = Button(interactables,text = "Update Preview", command= lambda:nt_update_preview(display,nt_name.get(),int(nt_y_position.get()),nt_font.get(),nt_font_size.get(),nt_font_color.get()),font = "Arial", bg = "#20bebe",fg = "white",height = 1,width=15)

#ELEMENTS FOR LABELS
#labels
lbl_name_label = Label(interactables, text="Name: ", font=("Raleway", 10))
lbl_school_label = Label(interactables, text="School: ", font=("Raleway", 10))
#text input
lbl_nameEntered = tk.StringVar()
lbl_nameEntered = ttk.Entry(interactables, width = 15, textvariable = lbl_nameEntered)
lbl_schoolEntered = tk.StringVar()
lbl_schoolEntered = ttk.Entry(interactables, width = 15, textvariable = lbl_schoolEntered)
#open csv button
lbl_csv_btn = Button(interactables,text = "Open CSV", command= lambda:open_csv(interactables),font = "Arial", bg = "#20bebe",fg = "white",height = 1,width=15)
#buttons
lbl_browse_btn = Button(interactables, text="Browse", command= lambda:lbl_open_imagefile(display,lbl_nameEntered.get(),lbl_schoolEntered.get()), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
lbl_save_pdf_btn = Button(interactables,text = "Save As PDF", command= lambda:lbl_save_as_pdf(lbl_nameEntered.get(),lbl_schoolEntered.get()),font = "Arial", bg = "#20bebe",fg = "white",height = 1,width=15)

#ELEMENTS FOR CERTIFICATES
#labels
ctf_name_label = Label(interactables, text="Text: ", font=("Raleway", 10))
ctf_x_position_label = Label(interactables, text="Text X Position: ", font=("Raleway", 10))
ctf_y_position_label = Label(interactables, text="Text Y Position: ", font=("Raleway", 10))
ctf_font_label = Label(interactables, text="Text Font: ", font=("Raleway", 10))
ctf_font_size_label = Label(interactables, text="Text Font Size: ", font=("Raleway", 10))
ctf_font_color_label = Label(interactables, text="Text Color: ", font=("Raleway", 10))
#text input
ctf_name = tk.StringVar()
ctf_nameEntered = ttk.Entry(interactables, width = 15, textvariable = ctf_name)
#open csv button
ctf_csv_btn = Button(interactables,text = "Open CSV", command= lambda:open_csv(interactables),font = "Arial", bg = "#20bebe",fg = "white",height = 1,width=15)
#x potition text input
ctf_x_position = tk.StringVar(value = "110")
ctf_x_position = ttk.Entry(interactables, width = 15, textvariable = ctf_x_position)
ctf_x_position.insert(END, "110")
#y potition text input
ctf_y_position = tk.StringVar(value = "60")
ctf_y_position = ttk.Entry(interactables, width = 15, textvariable = ctf_y_position)
ctf_y_position.insert(END, "60")
#font text input
ctf_font = tk.StringVar(value = "times")
ctf_font = ttk.Entry(interactables, width = 15, textvariable = nt_font)
ctf_font.insert(END, "times")
#font size text input
ctf_font_size = tk.StringVar(value = "10")
ctf_font_size = ttk.Entry(interactables, width = 15, textvariable = nt_font_size)
ctf_font_size.insert(END, "10")
#font color text input
ctf_font_color = tk.StringVar(value = "#000000")
ctf_font_color = ttk.Entry(interactables, width = 15, textvariable = nt_font_color)
ctf_font_color.insert(END, "#000000")
#buttons
ctf_browse_btn = Button(interactables, text="Browse", command= lambda:ctf_open_imagefile(display,ctf_name.get(),ctf_x_position.get(),ctf_y_position.get(),ctf_font.get(),ctf_font_size.get(),ctf_font_color.get()), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
ctf_save_pdf_btn = Button(interactables,text = "Save As PDF", command= lambda:ctf_save_as_pdf(ctf_name.get(),int(ctf_x_position.get()),int(ctf_y_position.get()),ctf_font.get(),ctf_font_size.get(),ctf_font_color.get()),font = "Arial", bg = "#20bebe",fg = "white",height = 1,width=15)
ctf_update_preview_btn = Button(interactables,text = "Update Preview", command= lambda:ctf_update_preview(display,ctf_name.get(),int(ctf_x_position.get()),int(ctf_y_position.get()),ctf_font.get(),ctf_font_size.get(),ctf_font_color.get()),font = "Arial", bg = "#20bebe",fg = "white",height = 1,width=15)

def clear_grid():
    for widget in interactables.grid_slaves():
        if int(widget.grid_info()["row"]) > 0:
            widget.grid_forget()

def update(*args):
    global update_in_progress
    if update_in_progress: return
    try:
        format_option_temp = format_option.get()
    except ValueError:
        return

    if format_option_temp == "Nametag":
        #gridding for interactables frame
        clear_grid()
        question_menu.grid(column = 2, row = 1)
        nt_nameEntered.grid(column = 2, row = 2)
        nt_y_position.grid(column = 2, row = 4)
        nt_font.grid(column = 2, row = 5, pady = 10)
        nt_font_size.grid(column = 2, row = 6, pady = 10)
        nt_font_color.grid(column = 2, row = 7, pady = 10)
        nt_browse_btn.grid(column=2, row=8,pady=10)
        nt_csv_btn.grid(column = 2, row = 9, pady = 10)
        nt_save_pdf_btn.grid(column = 2, row = 10, pady = 10)
        nt_update_preview_btn.grid(column = 2, row = 11, pady = 10)

        #gridding for labels
        nt_name_label.grid(column = 1,row=2)
        nt_y_position_label.grid(column = 1,row=4)
        nt_font_label.grid(column = 1,row=5)
        nt_font_size_label.grid(column = 1,row=6)
        nt_font_color_label.grid(column = 1,row=7)

    if format_option_temp == "Label":
        #gridding for interactables frame
        clear_grid()
        question_menu.grid(column = 2, row = 1)
        lbl_nameEntered.grid(column = 2, row = 2)
        lbl_schoolEntered.grid(column = 2, row = 3)
        lbl_browse_btn.grid(column=2, row=4,pady=10)
        lbl_csv_btn.grid(column = 2, row = 5, pady = 10)
        lbl_save_pdf_btn.grid(column = 2, row = 6, pady = 10)
        #gridding for labels
        lbl_name_label.grid(column = 1,row=2)
        lbl_school_label.grid(column = 1,row=3)

    if format_option_temp == "Certificate":
        #gridding for interactables frame
        clear_grid()
        question_menu.grid(column = 2, row = 1)
        ctf_nameEntered.grid(column = 2, row = 2)
        ctf_x_position.grid(column = 2, row = 3)
        ctf_y_position.grid(column = 2, row = 4)
        ctf_font.grid(column = 2, row = 5, pady = 10)
        ctf_font_size.grid(column = 2, row = 6, pady = 10)
        ctf_font_color.grid(column = 2, row = 7, pady = 10)
        ctf_browse_btn.grid(column=2, row=8,pady=10)
        ctf_csv_btn.grid(column = 2, row = 9, pady = 10)
        ctf_save_pdf_btn.grid(column = 2, row = 10, pady = 10)
        ctf_update_preview_btn.grid(column = 2, row = 11, pady = 10)
        #gridding for labels
        ctf_name_label.grid(column = 1,row=2)
        ctf_x_position_label.grid(column = 1,row=3)
        ctf_y_position_label.grid(column = 1,row=4)
        ctf_font_label.grid(column = 1,row=5)
        ctf_font_size_label.grid(column = 1,row=6)
        ctf_font_color_label.grid(column = 1,row=7)



format_option.trace_add('write', update)




root.mainloop()
