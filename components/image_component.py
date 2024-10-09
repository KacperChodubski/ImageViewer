import tkinter as tk
from PIL import Image, ImageTk

class ImageComponent():
    def __init__(self, window) -> None:
        self.window = window
        self.label = tk.Label(self.window)

    def showImage(self, image, functions=None):
        if functions is not None:
            for f in functions:
                if f is not None:
                    image = f(image)
                    # print('processed', f)
        if image is not None:
            self.img = ImageTk.PhotoImage(image)
            self.label.destroy()
            self.label = tk.Label(self.window, image=self.img)
            self.label.pack(side=tk.LEFT, padx=50)
