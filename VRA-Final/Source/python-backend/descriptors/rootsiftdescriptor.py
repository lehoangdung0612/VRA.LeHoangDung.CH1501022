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
 
        if len(kps) == 0:
            return ([], None)
 
        # apply the Hellinger kernel by first L1-normalizing and taking the
        # square-root
        descs /= (descs.sum(axis=0) + eps)
        descs = np.sqrt(descs)
        descs /= (np.linalg.norm(descs, axis=0, ord=2) + eps)
 
        return (kps, descs)