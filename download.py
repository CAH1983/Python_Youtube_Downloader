from tkinter import *
from tkinter import filedialog

screen = Tk()
title = screen.title('Youtube downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='./Images/YouTube-logo-PNG-HD-1024x928.png')

# resize
logo_img = logo_img.subsample(2, 2)

canvas.create_image(255, 80, image=logo_img)

screen.mainloop()