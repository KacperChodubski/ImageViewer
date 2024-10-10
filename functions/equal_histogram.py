from PIL import ImageFilter, Image
from .function import Function

class EqualHistogram(Function):
    def __init__(self) -> None:
        self.name = "Equal histogram"

    def process(self, image: Image.Image) -> Image.Image:
        values = image.histogram()
        lut = []
        for i in range(256):
            lut.append(sum(values[:i+1]) * 255 // sum(values))
        return image.point(lut)
