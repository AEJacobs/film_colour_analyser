#! python3

import numpy as np


def create_blank(new_width, new_height, bgr_color=(0, 0, 0)):
    """Create and return new image(numpy array) filled with certain color in BGR (for working with OpenCV"""
    new_image = np.zeros((new_width, new_height, 3), np.uint8) # Create black blank image
    new_image[:] = bgr_color     # Fill image with color
    return new_image
