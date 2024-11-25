import math
import numpy as np
from PIL import Image

class PEAttributeExtractor():

    def __init__(self, bytez):
        self.bytez = bytez
        self.IMG_SIDE = 128

    def best_fit_size(self):
        normalized_data = np.frombuffer(self.bytez, dtype=np.uint8)
        num_pixels = len(normalized_data) 
        side_length = int(math.sqrt(num_pixels))
        return side_length

    def bytes_to_grayscale_image(self, side_length):
        normalized_data = np.frombuffer(self.bytez, dtype=np.uint8)
        if len(normalized_data) < side_length * side_length:
            upsampled_data = np.zeros((side_length * side_length,), dtype=np.uint8)
            upsampled_data[:len(normalized_data)] = normalized_data
            image_data = upsampled_data.reshape((side_length, side_length))
        elif len(normalized_data) > side_length * side_length:
            image_data = normalized_data[:side_length * side_length].reshape((side_length, side_length))
        else:
            image_data = normalized_data.reshape((side_length, side_length))
        
        image_bw = Image.fromarray(image_data, 'L')
        img = image_bw.resize((self.IMG_SIDE, self.IMG_SIDE), Image.Resampling.LANCZOS)
        return img
    
    def extract(self):
        length = self.best_fit_size()
        return self.bytes_to_grayscale_image(length)