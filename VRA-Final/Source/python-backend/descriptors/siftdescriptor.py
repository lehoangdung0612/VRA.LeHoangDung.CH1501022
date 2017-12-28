# import the necessary packages
import numpy as np
import cv2

class SIFT:
    def __init__(self):
        self.detector = cv2.xfeatures2d.SIFT_create()
        return;

    def describe(self, image):
        (kps, descs) = self.detector.detectAndCompute(image, None)

        if len(kps) == 0:
            return ([], None)

        return (kps, descs)
