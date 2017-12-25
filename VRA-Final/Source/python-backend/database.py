# import the necessary packages
import numpy as np
import cv2
import os
from sklearn.externals import joblib

class DataBase:
	def __init__(self):
		return

	def write(self, file, data):
		print "Storing data in file: {}".format(file)
		joblib.dump(data, file, compress=5)
		return

	def read(self, file):
		print "Loading data from file: {}".format(file)
		data = joblib.load(file)
		return data

	def checkFile(self, file):
		return os.path.isfile(file)