from .regular_button import RegularButton
from .label import Label
from .image_component import ImageComponent
from .file_selector import FileSelector
from .select_list import SelectList
from tkinter import messagebox

class LoadImageWindow:
    def __init__(self, window, parent) -> None:
        self.window = window
        self.parent = parent
        self.file_selector = FileSelector()
        self.image_component = ImageComponent(window=window)
        self.image_component2 = ImageComponent(window=window)
        self.file_selector.addCallback(lambda: self.image_component.showImage(self.file_selector.getFilePath()))
        self.file_selector.addCallback(lambda: self.image_component2.showImage(self.file_selector.getFilePath()))

        self.components = []
        self.components.append(RegularButton(window=window, text="<- Back", command=parent.load))
        self.components.append(RegularButton(window=window, text="Load image", command=self.file_selector.selectFile))
        self.components.append(Label(window=window, text="Select process function", font_size=10))
        self.components.append(SelectList(window=window, values=["test1", "test2", "test3"]))

    def load(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        for component in self.components:
            component.load()
