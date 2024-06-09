import tkinter as tk
from tkinter import ttk
from hacking_tools import HackingTools
from packet_tools import PacketTools
from mp3_player import MP3Player
from youtube_downloader import YouTubeDownloader
from port_scanner import PortScanner
from internet_radio import InternetRadio

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Function Application")
        self.geometry("800x600")

        self.tabControl = ttk.Notebook(self)

        self.hacking_tools_tab = HackingTools(self.tabControl)
        self.packet_tools_tab = PacketTools(self.tabControl)
        self.mp3_player_tab = MP3Player(self.tabControl)
        self.youtube_downloader_tab = YouTubeDownloader(self.tabControl)
        self.port_scanner_tab = PortScanner(self.tabControl)
        self.internet_radio_tab = InternetRadio(self.tabControl)

        self.tabControl.add(self.hacking_tools_tab, text="Hacking Tools")
        self.tabControl.add(self.packet_tools_tab, text="Packet Tools")
        self.tabControl.add(self.mp3_player_tab, text="MP3 Player")
        self.tabControl.add(self.youtube_downloader_tab, text="YouTube Downloader")
        self.tabControl.add(self.port_scanner_tab, text="Port Scanner")
        self.tabControl.add(self.internet_radio_tab, text="Internet Radio")

        self.tabControl.pack(expand=1, fill="both")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()