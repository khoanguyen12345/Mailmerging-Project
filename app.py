import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageDraw
from functions import save_as_pdf,open_imagefile,open_csv
import os


root = tk.Tk()
root.geometry('+%d+%d'%(350,10))

#interactables frame
interactables = Frame(root,height=200,width=200)
interactables.grid(columnspan=3, rowspan=10, row=0,column=0)

#display frame
display = Frame(root,height = 200,width=200)
display.grid(columnspan = 2, rowspan = 2,row=4,column=6)

#options menu (checklist format)
options_list = ["Nametag", "Label", "Certificate"]
format_option = tk.StringVar(interactables)
format_option.set("Select an Option")
question_menu = tk.OptionMenu(interactables, format_option, *options_list)

#labels
name_label = Label(interactables, text="Text: ", font=("Raleway", 10))
x_position_label = Label(interactables, text="X Position: ", font=("Raleway", 10))
y_position_label = Label(interactables, text="Y Position: ", font=("Raleway", 10))

#text input
name = tk.StringVar()
nameEntered = ttk.Entry(interactables, width = 15, textvariable = name)

#open csv button
csv_btn = Button(interactables,text = "Open CSV", command= lambda:open_csv(interactables),font = "Arial", bg = "#20bebe",fg = "white",height = 1,width=15)

#x potition text input
x_position = tk.StringVar(value = "150")
x_position = ttk.Entry(interactables, width = 15, textvariable = x_position)
x_position.insert(END, "150")

#y potition text input
y_position = tk.StringVar(value = "70")
y_position = ttk.Entry(interactables, width = 15, textvariable = y_position)
y_position.insert(END, "70")

#buttons
browse_btn = Button(interactables, text="Browse", command= lambda:open_imagefile(display,name.get(),x_position.get(),y_position.get()), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
save_pdf_btn = Button(interactables,text = "Save As PDF", command= lambda:save_as_pdf(name.get(),int(x_position.get()),int(y_position.get()),format_option.get()),font = "Arial", bg = "#20bebe",fg = "white",height = 1,width=15)

#gridding for interactables frame
question_menu.grid(column = 2, row = 1)
nameEntered.grid(column = 2, row = 2)
x_position.grid(column = 2, row = 3)
y_position.grid(column = 2, row = 4)
browse_btn.grid(column=2, row=5,pady=10)
csv_btn.grid(column = 2, row = 6, pady = 10)
save_pdf_btn.grid(column = 2, row = 7, pady = 10)


#gridding for labels
name_label.grid(column = 1,row=2)
x_position_label.grid(column = 1,row=3)
y_position_label.grid(column = 1,row=4)


root.mainloop()
