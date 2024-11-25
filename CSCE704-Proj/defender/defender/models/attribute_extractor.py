import math
import numpy as np
from PIL import Image

class PEAttributeExtractor():

    def __init__(self, bytez):
        self.bytez = bytez
        self.IMG_SIDE = (128, 128)

    def bytes_to_rgb_image(self):
        byte_array = np.frombuffer(self.bytez, dtype=np.uint8)
        side_length = int(np.ceil(np.sqrt(len(byte_array))))
        padded_array = np.zeros(side_length ** 2, dtype=np.uint8)
        padded_array[:len(byte_array)] = byte_array
        square_image = padded_array.reshape((side_length, side_length))

        image = Image.fromarray(square_image, mode='L').convert('RGB')
        image = image.resize(self.IMG_SIDE)

        return np.expand_dims(np.array(image) / 255.0, axis=0)
    
    def extract(self):
        img = self.bytes_to_rgb_image()
        return img