# import the necessary packages
import numpy as np
import cv2

class RootSIFT:
    def __init__(self):
        # initialize the SIFT feature extractor
        self.detector = cv2.xfeatures2d.SIFT_create()
 
    def describe(self, image, eps=1e-7):
        # compute SIFT descriptors
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (kps, descs) = self.detector.detectAndCompute(image, None)
 
        # if there are no keypoints or descriptors, return an empty tuple
        if len(kps) == 0:
            return ([], None)
 
        # apply the Hellinger kernel by first L1-normalizing, taking the
        # square-root
        descs /= (descs.sum(axis=1, keepdims=True) + eps)
        descs = np.sqrt(descs)

        return (kps, descs)