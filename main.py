import tkinter as tk
from components import *
from scipy import ndimage
import numpy as np
from PIL import ImageFilter
from functions import *

class Main:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.start_app()
    
    def select_filter(self, function):
        self.selected_function = function
        self.reload_images()
    def reload_images(self):
        self.image_component.showImage(self.file_selector.getImage())
        self.processed_image.showImage(self.file_selector.getImage(), [self.selected_function])
        self.histogram_component.showImage(self.file_selector.getImage(), [self.selected_function, self.histogram.process])

    def close_main_window(self):
        self.window.destroy()

    def start_app(self):
        # Create the main window
        self.window.title("")

        # Set the window size (Width x Height)
        self.window.geometry("1400x1000")
        # MainWindow(window=window).load()
        sobel_filter = SobelFilter()
        gaussian_filter = GaussianFilter()
        change_brightness = ChangeBrightness()
        negative_f = Negative()
        powering = Powering()
        equal_hist = EqualHistogram()
        self.histogram = Histogram()
        self.image_component = ImageComponent(window=self.window)
        self.processed_image = ImageComponent(window=self.window)
        self.histogram_component = ImageComponent(window=self.window)
        self.selected_function: Function | None = None


        self.file_selector = FileSelector()


        values = [
                SelectItem("Default", lambda: self.select_filter(None)),
                SelectItem(sobel_filter.name, lambda: self.select_filter(sobel_filter.process)),
                SelectItem(gaussian_filter.name, lambda: self.select_filter(gaussian_filter.process)),
                SelectItem(change_brightness.name, lambda: self.select_filter(change_brightness.process)),
                SelectItem(negative_f.name, lambda: self.select_filter(negative_f.process)),
                SelectItem(powering.name, lambda: self.select_filter(powering.process)),
                SelectItem(equal_hist.name, lambda: self.select_filter(equal_hist.process)),
        ]
        self.file_selector.addCallback(self.reload_images)
        self.file_selector.addCallback(self.reload_images)
        self.file_selector.addCallback(self.reload_images)
        self.select_list = SelectList(window=self.window, values=values)

        components = []
        components.append(RegularButton(window=self.window, text="Load image", command=self.file_selector.selectFile))
        components.append(Label(window=self.window, text="Select process function", font_size=10))
        components.append(self.select_list)
        components.append(RegularButton(window=self.window, text="Select", command=self.select_list.callSelected))
        for component in components:
            component.load()

        # Start the GUI event loop
        self.window.mainloop()


if __name__ == '__main__':
    Main()
