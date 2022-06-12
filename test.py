from tkinter import *
from PIL import Image, ImageTk

root = Tk()
bck = Image.open("train.png")

background = ImageTk.PhotoImage(image=bck)
background_label = Label(image=background)
background_label.pack()

root.mainloop()