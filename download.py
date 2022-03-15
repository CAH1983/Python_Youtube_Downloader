from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import subprocess
from pytube import Playlist
import shutil
import ffmpy

# functions


def select_path():
    # filedialog allows so select a file from a directory
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_1file_MP4():
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


# download whole playlist in MP3 audio
def download_playlist_MP4():
    print('Downloading playlist MP4 ...')
    screen.title('started downloading playlist ...')
    playlist_link = link_field.get()
    # get user path
    user_directory = path_label.cget('text')
    playlist = Playlist(playlist_link)
    # looping through each video
    for video in playlist.videos:
        print('Downloading: {} with url: {}'.format(
            video.title, video.watch_url))
        screen.title('downloading ...')
        video.streams.\
            filter(only_audio=True).\
            first().\
            download(user_directory)
    print('finished downloading!')


def download_playlist_MP3():
    print('Downloading playlist MP3 ...')


# styling
font_color = 'white'
background_color = '#1b4965'
screen = Tk()
title = screen.title('Youtube downloader')
canvas = Canvas(screen, width=500, height=700, bg=background_color)
canvas.pack()

# image logo
logo_img = PhotoImage(file='./Images/YouTube-logo-PNG-HD-1024x928.png')

# resize
logo_img = logo_img.subsample(3, 3)

canvas.create_image(255, 180, image=logo_img)

# configure the label and URL input for  download
link_label = Label(
    screen, text='Enter / Paste link to download: ', font=('Arial', 15), bg=background_color, fg=font_color)
link_field = Entry(screen, width=50)


# Add label and input to window
canvas.create_window(250, 380, window=link_label)
canvas.create_window(250, 420, window=link_field)

# Select path for where to save the file on the computer
path_label = Label(screen, text='Select path for download', font=(
    'Arial', 13),  bg=background_color, fg=font_color)
select_btn = Button(screen, text='Select', command=select_path)

canvas.create_window(250, 460, window=path_label)
canvas.create_window(250, 490, window=select_btn)

download_1File_MP4_btn = Button(screen, text="Download only 1 File MP4",
                                command=download_1file_MP4, bg='#cae9ff')

download_playlist_MP4_btn = Button(
    screen, text="Download Full Playlist MP4", bg='#ffd5c2', command=download_playlist_MP4)

download_playlist_MP3_btn = Button(
    screen, text="Download Full Playlist MP3", bg='#ffd5c2', command=download_playlist_MP3)

canvas.create_window(250, 540, window=download_1File_MP4_btn)
canvas.create_window(250, 570, window=download_playlist_MP4_btn)
canvas.create_window(250, 600, window=download_playlist_MP3_btn)
screen.mainloop()
