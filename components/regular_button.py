import tkinter as tk
from tkinter import messagebox, filedialog

class RegularButton:
    def __init__(self, window, text, command) -> None:
        self.window = window
        self.text = text
        self.command = command

    def load(self):
        tk.Button(self.window, text=self.text, command=self.command).pack(pady=5)
