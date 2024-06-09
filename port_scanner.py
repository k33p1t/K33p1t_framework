import tkinter as tk
from tkinter import ttk
import nmap

class PortScanner(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Port Scanner")
        self.label.pack(pady=10)
        
        self.host_entry = tk.Entry(self, width=50)
        self.host_entry.pack(pady=5)
        
        self.scan_button = tk.Button(self, text="Scan", command=self.scan_ports)
        self.scan_button.pack(pady=5)
        
        self.result_text = tk.Text(self, height=20, width=80)
        self.result_text.pack(pady=5)
        
    def scan_ports(self):
        nm = nmap.PortScanner()
        host = self.host_entry.get()
        nm.scan(host)
        result = nm.csv()
        self.result_text.insert(tk.END, result)