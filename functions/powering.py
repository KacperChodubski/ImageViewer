from PIL import ImageFilter, Image
from .function import Function
import numpy as np

class Powering(Function):
    def __init__(self) -> None:
        self.name = "Powering"

    def process(self, image) -> Image.Image:
        return image.point(lambda x: 255 * pow(x/255, 2))
