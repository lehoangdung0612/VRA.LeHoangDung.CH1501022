# USAGE
# python index.py

# import the necessary packages
import glob
import cv2
import argparse
import numpy as np
import scipy.cluster
import sklearn.cluster

from sklearn import preprocessing
import math
import traceback

from database import DataBase
from config import Config
from descriptors.feature import Descriptor

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--feature", help = "Feature for extraction")
ap.add_argument("-t", "--type", help = "KMeans type for clustering")
args = vars(ap.parse_args())


def extractFeatures(descriptorMethod, feature, imageFiles):
    image_paths = []
    des_list = []
    descriptors = []

    for i, imagePath in enumerate(imageFiles):
        imagePath = imagePath.replace("\\", "/")
        imageID = imagePath[imagePath.rfind("/") + 1:]
        image = cv2.imread(imagePath)

        # describe the image
        print "Extracting {} of {}, image of {}/{}".format(feature.upper(), imageID, i+1, len(imageFiles))
        (kps, data) = descriptorMethod.extractFeatures(feature, image)

        if len(kps) > 0:
            # Create descriptors
            image_paths += [imagePath]
            des_list.append(data)

            if (len(des_list) == 1):
                descriptors = des_list[0]
            else:
                descriptors = np.vstack((descriptors, data))

    return (image_paths, des_list, descriptors)


def createDescriptors(des_list, imageFiles):
    print "Creating descriptors of {} images".format(len(imageFiles))
    descriptors = des_list[0]
    for descriptor in des_list[1:]:
        descriptors = np.vstack((descriptors, descriptor))
    return descriptors


def kMeansClustering(kmeansType, descriptors, numWords, iterations):
    print "Clustering k-means: %d words, %d descriptors" %(numWords, descriptors.shape[0])
    
    if kmeansType == 3:
        kmeans3 = sklearn.cluster.KMeans(n_clusters=numWords, max_iter=iterations)
        kmeans3.fit(descriptors)
        (voc, variance) = (kmeans3.cluster_centers_, kmeans3.labels_)
    elif kmeansType == 2:
        (voc, variance) = scipy.cluster.vq.kmeans2(descriptors.astype(float), numWords, iterations)
    else:
        (voc, variance) = scipy.cluster.vq.kmeans(descriptors.astype(float), numWords, iterations)
    return (voc, variance)


def calculateTFIDF(des_list, voc, variance, numWords, numImages):
    print "Calculating Tf-Idf vectorization of features"
    im_features = np.zeros((numImages, numWords), "float32")
    for i in xrange(numImages):
        # In kmeans, labels = scipy.cluster.vq.vq(ar, voc)
        words, _ = scipy.cluster.vq.vq(des_list[i], voc)

        for w in words:
            im_features[i][w] += 1

    # Perform Tf-Idf vectorization
    nbr_occurences = np.sum( (im_features > 0) * 1, axis = 0)
    idf = np.array(np.log((1.0*numImages+1) / (1.0*nbr_occurences + 1)), 'float32')

    # Perform L2 normalization
    im_features = im_features*idf
    im_features = preprocessing.normalize(im_features, norm='l2')
    return (im_features, idf)


def main():
    try:
        # initialize variable
        db = DataBase()
        settings = Config.Settings
        if args["feature"] is None:
            feature = settings["FEATURE"]
        else:
            feature = args["feature"]

        if args["type"] is None:
            kmeansType = Config.KMeans["TYPE"]
        else:
            kmeansType = args["type"]

        filename = "{}/{}_{}_kmeans{}_{}".format(settings["ROOT_DATASET_FOLDER"], settings["TRAIN_DATASET"], feature, kmeansType, settings["FEATURE_FILE"])

        if db.checkFile(filename):
            (image_paths, im_features, idf, numWords, voc) = db.read(filename)
        else:
            descriptorHandler = Descriptor(Config)
            numWords = Config.KMeans["NUM_WORDS"]
            iterations = Config.KMeans["ITER"]
            imageFiles = glob.glob("{}/{}/*.*".format(settings["ROOT_DATASET_FOLDER"], settings["TRAIN_DATASET"]))

            if len(imageFiles) > settings["MAX_FILES"]:
                np.random.shuffle(imageFiles)
                imageFiles = imageFiles[:settings["MAX_FILES"]]

            # Extract features of images
            (image_paths, des_list, descriptors) = extractFeatures(descriptorHandler, feature, imageFiles)

            # Create descriptors
            # descriptors = createDescriptors(des_list, imageFiles);
                
            # Perform k-means clustering
            if (descriptors.shape[0] / numWords) < 100:
                numWords = numWords / 100
            (voc, variance) = kMeansClustering(kmeansType, descriptors, numWords, iterations)

            # Calculate the TF-IDF of features
            filename = "{}/{}_{}_kmeans{}_{}".format(settings["ROOT_DATASET_FOLDER"], settings["TRAIN_DATASET"], feature, kmeansType, settings["FEATURE_FILE"])
            (im_features, idf) = calculateTFIDF(des_list, voc, variance, numWords, len(image_paths))
            db.write(filename, (image_paths, im_features, idf, numWords, voc))

    except Exception as e:
        tb = traceback.format_exc()
        print 'Error found: %s' % (tb)


if __name__ == "__main__":
    main()


