from PIL import ImageFilter, Image
from .function import Function
import numpy as np

class ChangeBrightness(Function):
    def __init__(self) -> None:
        self.name = "Change brightness"

    def process(self, image: Image.Image):

        # array = np.array(image, dtype=np.uint16) * 2 + 20
        # array = np.clip(array, 0, 255)
        # image = Image.fromarray(array)
        return image.point(lambda x: (x*2) + 20)
