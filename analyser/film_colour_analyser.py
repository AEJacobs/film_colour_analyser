#! python3
"""
This uses openCV to analyse a film and output the average colour of frames from the film
It takes those values and compiles an image to visually represent them in sequence
TODO - Export the result set data so you don't have to re-analyse films at the same sample rate
TODO - collect top 5 colours per capture
TODO - analyse the most common 5 colours for the whole film and save as a colour palette image
TODO - Get it to detect scenes and give dominant colour for each scene
"""

import numpy as np
import cv2
import create_image
import time
from pathlib import Path


class Analyser:
    def __init__(self, filename, output_location):
        self.film = filename
        self.vidcap = cv2.VideoCapture(self.film)
        self.results = []
        self.output_location = output_location
        self.width, self.height = 300, 2
        self.final_output = np.zeros((self.width, self.height, 3), np.uint8)

    def analyse(self):
        print('Now processing: ' + self.film)
        start = time.time()
        sec = 0
        frame_rate = 5  # it will capture image in each n seconds
        count = 1
        success = self.get_frame(sec)

        while success:
            count = count + 1
            sec = sec + frame_rate
            sec = round(sec, 2)
            success = self.get_frame(sec)

        self.save_output()
        end = time.time()
        duration = end - start
        # print('Processing complete! Time taken: ' + str(duration.__round__(0)) + ' seconds')
        return 'Processing complete! Time taken: ' + str(duration.__round__(0)) + ' seconds'

    def get_frame(self, sec):
        self.vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
        has_frames, img = self.vidcap.read()
        if has_frames:
            self.process_frame(img)
        return has_frames

    def process_frame(self, img):
        n_colors = 5
        pixels = np.float32(img.reshape(-1, 3))
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        flags = cv2.KMEANS_RANDOM_CENTERS
        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        _, counts = np.unique(labels, return_counts=True)
        dominant = palette[np.argmax(counts)]
        frame_colour = create_image.create_blank(self.width, self.height, dominant)
        self.final_output = cv2.hconcat([self.final_output, frame_colour])
        self.results.append(dominant)

    def save_output(self):
        file_name = Path(self.film).stem
        image_string = self.output_location + '/' + file_name + '.jpg'
        cv2.imwrite(image_string, self.final_output)
