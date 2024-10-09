from PIL import ImageFilter, Image
import matplotlib.pyplot as plt
from .function import Function
import numpy as np
import io

class Histogram(Function):
    def __init__(self) -> None:
        self.name = "Histogram"

    def process(self, image: Image.Image):
        image = image.convert('L')
        values = image.histogram()
        values_sum = sum(values)
        values = list(map(lambda x: x/values_sum, values))
        i = list(range(0, 256, 1))
        plt.clf()
        plt.bar(i, values)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image = np.array(Image.open(buf))
        buf.close()
        size = (400, 400)
        image = Image.fromarray(image)
        image.thumbnail(size, Image.Resampling.LANCZOS)
        return image
