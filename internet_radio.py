import tkinter as tk
from tkinter import ttk
import pygame

class InternetRadio(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Internet Radio")
        self.label.pack(pady=10)
        
        pygame.mixer.init()
        
        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=5)
        
        self.play_button = tk.Button(self, text="Play", command=self.play_stream)
        self.play_button.pack(pady=5)
        
    def play_stream(self):
        url = self.url_entry.get()
        pygame.mixer.music.load(url)
        pygame.mixer.music.play()