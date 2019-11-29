import cv2
import numpy as np
import scipy as sp
import unittest
import os

import textures as tex

"""
You can use this file as a starting point to write your own unit tests
for this assignment. You are encouraged to discuss testing with your
peers, but you may not share code directly. Your code is scored based
on test cases performed by the autograder upon submission -- these test
cases will not be released.

    DO NOT SHARE CODE (INCLUDING TEST CASES) WITH OTHER STUDENTS.
"""

SOURCE_FOLDER = os.path.abspath(os.path.join(os.curdir, 'videos', 'source'))
EXTS = ['.bmp', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.jpeg', '.jpg',
        '.jpe', '.jp2', '.tiff', '.tif', '.png']


class Assignment11Test(unittest.TestCase):

    def setUp(self):
        for video_dir in os.listdir(SOURCE_FOLDER):
            img_list = []
            filenames = sorted(os.listdir(os.path.join(SOURCE_FOLDER, video_dir)))

            for filename in filenames:
                name, ext = os.path.splitext(filename)
                if ext in EXTS:
                    img_list.append(cv2.imread(os.path.join(SOURCE_FOLDER,
                                                            video_dir,
                                                            filename)))

        if any(img is None for img in img_list):
            raise IOError("Error reading one or more source images.")

        self.images = img_list


if __name__ == '__main__':
    unittest.main()
