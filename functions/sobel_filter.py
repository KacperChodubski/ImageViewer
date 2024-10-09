from PIL import ImageFilter
from .function import Function

class SobelFilter(Function):
    def __init__(self) -> None:
        self.name = "Sobel filter"

    def process(self, image):
        kernel = ImageFilter.Kernel(
                size=(3, 3),
                scale=1,
                kernel=( 0, -2,  0,
                        -2,  8, -2,
                         0, -2,  0))
        return image.filter(kernel)
