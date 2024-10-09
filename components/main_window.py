import tkinter as tk
from .regular_button import RegularButton
from .label import Label
from .load_image_window import LoadImageWindow

class MainWindow:
    def __init__(self, window) -> None:
        self.window = window
        self.load_image_window = LoadImageWindow(window, self)

        self.components = []
        self.components.append(RegularButton(self.window, text="Load image", command=self.load_image_window.load))

    def load(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        for component in self.components:
            component.load()
