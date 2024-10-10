from PIL import ImageFilter, Image
from .function import Function
import numpy as np

class Negative(Function):
    def __init__(self) -> None:
        self.name = "Negative"

    def process(self, image) -> Image.Image:
        return image.point(lambda x: 255 - x)
