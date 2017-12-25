# import the necessary packages
from surfdescriptor import SURF
from siftdescriptor import SIFT
from rootsiftdescriptor import RootSIFT

class Descriptor:
    def __init__(self, config):
        descriptors = {};
        descriptors[config.Features["SURF"]] = SURF()
        descriptors[config.Features["SIFT"]] = SIFT()
        descriptors[config.Features["ROOTSIFT"]] = RootSIFT()
        self.descriptors = descriptors;

    def extractFeatures(self, feature, image):
        (kps, descs) = self.descriptors[feature].describe(image)
        return (kps, descs)