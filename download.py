from tkinter import *
from tkinter import filedialog

screen = Tk()
title = screen.title('Youtube downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# image logo
logo_img = PhotoImage(file='./Images/YouTube-logo-PNG-HD-1024x928.png')

# resize
logo_img = logo_img.subsample(3, 3)

canvas.create_image(255, 100, image=logo_img)

# configure the label and input
link_field = Entry(screen, width=50)
link_label = Label(
    screen, text='Enter / Paste link to download: ', font=('Arial', 15))

# Add label and input to window
canvas.create_window(250, 260, window=link_label)
canvas.create_window(250, 290, window=link_field)

# Select path for where to save the file on the computer
path_label = Label(screen, text='Select path for download', font=('Arial', 13))
select_btn = Button(screen, text='Select')

canvas.create_window(250, 320, window=path_label)
canvas.create_window(250, 350, window=select_btn)

download_btn = Button(screen, text="Download File")

canvas.create_window(250, 400, window=download_btn)
screen.mainloop()
