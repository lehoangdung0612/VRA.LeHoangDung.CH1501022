#!/usr/local/bin/python2.7
#python search.py -i dataset/image.jpg

import cv2
import traceback
import urllib
import numpy as np
from scipy.cluster.vq import *
from sklearn import preprocessing

from database import DataBase
from config import Config
from descriptors.feature import Descriptor

# Load the classifier, class names, scaler, number of clusters and vocabulary (voc)
db = DataBase()
descriptorHandler = Descriptor(Config)
settings = Config.Settings
Datasets = {}

for key, value in Config.Features.iteritems():
    filename = "{}/{}_{}_kmeans{}_{}".format(settings["ROOT_DATASET_FOLDER"], settings["TRAIN_DATASET"], value, Config.KMeans["TYPE"], settings["FEATURE_FILE"])
    if db.checkFile(filename):
        (image_paths, im_features, idf, numWords, voc) = db.read(filename)
        Datasets[value] = (image_paths, im_features, idf, numWords, voc)


def getQueryImage(image_path, cx=0, cy=0, cw=0, ch=0):
    if image_path.find("http") != -1:
        imgdata = urllib.urlopen(image_path)
        arr = np.asarray(bytearray(imgdata.read()), dtype = np.uint8)
        query = cv2.imdecode(arr, -1)
    else:
        if (image_path.find("/") == -1) and (image_path.find("\\") == -1):
            query = cv2.imread("{}/{}".format(Config.Resources["UPLOAD_FOLDER"], image_path))
        else:
            query = cv2.imread(image_path)

    if (cx and cy and cw and ch):
        query = query[cy:cy + ch, cx:cx + cw]

    return query

def createDescriptors(descriptorMethod, feature, query):
    (_, data) = descriptorMethod.extractFeatures(feature, query)
    return data

def calculateTFIDF(descriptors, idf, voc, numWords):
    test_features = np.zeros((1, numWords), "float32")
    (words, distance) = vq(descriptors, voc)
    for w in words:
        test_features[0][w] += 1

    # Perform Tf-Idf vectorization and L2 normalization
    test_features = test_features*idf
    test_features = preprocessing.normalize(test_features, norm='l2')
    return test_features

def ranking(test_features, im_features, searchResult):
    score = np.dot(test_features, im_features.T)
    rank_ID = np.argsort(-score[0])
    # sorted decending score
    decScore = sorted(score[0], reverse=True)
    # reduce ranking
    rank_ID = rank_ID[:searchResult]
    return (rank_ID, decScore)

def searchImage(q, feature, cx=0, cy=0, cw=0, ch=0):
    try:
        searchResult = settings["SEARCH_RESULT"]
        if (feature is None):
            feature = settings["FEATURE"]

        # load data features
        (image_paths, im_features, idf, numWords, voc) = Datasets[feature]

        # load query image and crop
        query = getQueryImage(q, cx, cy, cw, ch)
       
        # create descriptors vertically in a numpy array
        descriptors = createDescriptors(descriptorHandler, feature, query)

        # Calculate the histogram of features
        test_features = calculateTFIDF(descriptors, idf, voc, numWords)

        # get distances and ranking result list
        (rank_ID, decScore) = ranking(test_features, im_features, searchResult)

        result = []
        for i, ID in enumerate(rank_ID):
            result += [{
                "image": image_paths[ID],
                "score": float(min(decScore[i], 1))
            }]

        return result
            
    except Exception as e:
        tb = traceback.format_exc()
        print 'Error found: %s' % (tb)
        return None
