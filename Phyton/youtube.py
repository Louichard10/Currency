from pytube import YouTube
import tkinter as tk
from tkinter import filedialog 

def download_video(url, save_path):
    try: 
        yt = YouTube(url)
        steams = yt.steams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = stream.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded to successfully!")
    except Exception as e:
        print(e)

url = "https://www.youtube.com/watch?v=qKfD4rY7HXI" 
save_path = "C:/Users/louichardbenjamin/Desktop/Phyton"

download_video(url, save_path)