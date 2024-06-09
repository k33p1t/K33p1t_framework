import tkinter as tk
from tkinter import ttk
from yt_dlp import YoutubeDL

class YouTubeDownloader(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="YouTube Downloader")
        self.label.pack(pady=10)
        
        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=5)
        
        self.download_button = tk.Button(self, text="Download", command=self.download_video)
        self.download_button.pack(pady=5)
        
    def download_video(self):
        url = self.url_entry.get()
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])