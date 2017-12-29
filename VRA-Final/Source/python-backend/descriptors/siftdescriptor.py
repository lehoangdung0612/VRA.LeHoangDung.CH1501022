# import the necessary packages
import numpy as np
import cv2

class SIFT:
    def __init__(self):
        self.detector = cv2.xfeatures2d.SIFT_create()
        return;

    def describe(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (kps, descs) = self.detector.detectAndCompute(image, None)

        if len(kps) == 0:
            return ([], None)

        return (kps, descs)
