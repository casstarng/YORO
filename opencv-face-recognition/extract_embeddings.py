# USAGE
# python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle \
# 	--detector face_detection_model --embedding-model openface_nn4.small2.v1.t7

# import the necessary packages
import pdb
from imutils import paths
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
                help="path to input directory of faces + images")
ap.add_argument("-e", "--embeddings", required=True,
	help="path to output serialized db of facial embeddings")
ap.add_argument("-d", "--detector", required=True,
	help="path to OpenCV's deep learning face detector")
ap.add_argument("-m", "--embedding-model", required=True,
                help="path to OpenCV's deep learning face embedding model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# load our serialized face detector from disk
# print("[INFO] loading face detector...")
# protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])
# modelPath = os.path.sep.join([args["detector"],
# 	"res10_300x300_ssd_iter_140000.caffemodel"])
# detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

# load our serialized face embedding model from disk
print("[INFO] loading face recognizer...")
embedder = cv2.dnn.readNetFromTorch(args["embedding_model"])

# # grab the paths to the input images in our dataset
# print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images(args["dataset"]))

# initialize our lists of extracted facial embeddings and
# corresponding people names
knownEmbeddings = []
knownNames = []

# initialize the total number of faces processed
total = 0

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
	name = imagePath.split(os.path.sep)[-2]

	image = cv2.imread(imagePath)

	# construct a blob for the face ROI, then pass the blob
	# through our face embedding model to obtain the 128-d
	# quantification of the face
	face = image
	faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                  (96, 96), (0, 0, 0), swapRB=True, crop=False)
	embedder.setInput(faceBlob)
	vec = embedder.forward()

	# add the name of the person + corresponding face
	# embedding to their respective lists
	knownNames.append(name)
	knownEmbeddings.append(vec.flatten())
	total += 1


# dump the facial embeddings + names to disk
print("[INFO] serializing {} encodings...".format(total))
data = {"embeddings": knownEmbeddings, "names": knownNames}
f = open(args["embeddings"], "wb")
f.write(pickle.dumps(data))
f.close()
