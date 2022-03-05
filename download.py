from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

# functions


def select_path():
    # filedialog allows so select a file from a directory
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    # Download video
    screen.title('Downloading ...')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)
    screen.title('Download complete! Download another file ..?')


# styling
font_color = 'white'
background_color = '#50808e'
screen = Tk()
title = screen.title('Youtube downloader')
canvas = Canvas(screen, width=500, height=500, bg=background_color)
canvas.pack()

# image logo
logo_img = PhotoImage(file='./Images/YouTube-logo-PNG-HD-1024x928.png')

# resize
logo_img = logo_img.subsample(3, 3)

canvas.create_image(255, 100, image=logo_img)

# configure the label and input
link_label = Label(
    screen, text='Enter / Paste link to download: ', font=('Arial', 15), bg=background_color, fg=font_color)
link_field = Entry(screen, width=50)

# Add label and input to window
canvas.create_window(250, 260, window=link_label)
canvas.create_window(250, 290, window=link_field)

# Select path for where to save the file on the computer
path_label = Label(screen, text='Select path for download', font=(
    'Arial', 13),  bg=background_color, fg=font_color)
select_btn = Button(screen, text='Select', command=select_path)

canvas.create_window(250, 320, window=path_label)
canvas.create_window(250, 360, window=select_btn)

download_btn = Button(screen, text="Download File",
                      command=download_file, bg='#cae9ff')

download_playlist_btn = Button(
    screen, text="Download Playlist", bg='#ffd5c2')

canvas.create_window(250, 400, window=download_btn)
canvas.create_window(250, 440, window=download_playlist_btn)
screen.mainloop()
