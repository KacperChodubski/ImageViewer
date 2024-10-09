from tkinter import filedialog
from PIL import Image, ImageTk
from constants import FORMATS_FOR_IMAGE

class FileSelector:
    def __init__(self) -> None:
        self.file_path = None
        self.image: Image.Image = None
        self.callbacks = []
        

    def addCallback(self, callback):
        self.callbacks.append(callback)

    def selectFile(self):
        filename = filedialog.askopenfilename(
                title="Select file",
                filetypes=[("Allowed files", FORMATS_FOR_IMAGE)]
        )
        if filename:
            self.file_path = filename
            self.image = Image.open(filename)
            size = (400, 400)
            self.image.thumbnail(size, Image.Resampling.LANCZOS)
        else:
            print("No file was selected.")

        for callback in self.callbacks:
            callback()

    def getFilePath(self):
        return self.file_path

    def getImage(self) -> Image.Image:
        return self.image
