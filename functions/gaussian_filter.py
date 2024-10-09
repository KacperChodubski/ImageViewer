from PIL import ImageFilter
from .function import Function

class GaussianFilter(Function):
    def __init__(self) -> None:
        self.name = "Gauss filer"

    def process(self, image):
        kernel = ImageFilter.Kernel(
                size=(3, 3),
                scale=32,
                kernel=( 1,  4,  1,
                         4, 12,  4,
                         1,  4,  1))
        return image.filter(kernel)
