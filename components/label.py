import tkinter as tk

class Label:
    def __init__(self, window, text, font_size) -> None:
        self.window = window
        self.text = text
        self.font_size = font_size

    def load(self):
        tk.Label(self.window, text=self.text, font=("Arial", self.font_size)).pack(pady=10)