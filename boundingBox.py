# Usage
# python boundingBox.py --detector opencv-face-recognition/face_detection_model --embedding-model opencv-face-recognition/openface_nn4.small2.v1.t7 --recognizer opencv-face-recognition/output/recognizer.pickle --le opencv-face-recognition/output/le.pickle

import cv2
import sys
import os
import argparse
import pickle
import imutils
import numpy as np
import logging as log
import datetime as dt
from time import sleep

from Faced.detector import FaceDetector
from Faced.utils import annotate_image

count = 0
user = "cassidy"

def crop_images(frame, bboxes):
    global count
    global user
    image = frame[:]
    img_h, img_w, _ = frame.shape
    cropped_images = []

    for x,y,w,h,p in bboxes:
        hei = int(h/2) + int(h/4)
        wei = int(w/2) + int(w/4)
        crop_img = frame[y-hei:y+hei, x-wei:x+wei].copy()

        cv2.imwrite('./opencv-face-recognition/dataset/'+user+'/' + user+str(count)+".jpg", crop_img)
        cropped_images.append((crop_img,x,y,w,h,p))
        count += 1

    return cropped_images

def main():
    #Initialize the Facial Recognition Neural Network
    face_detector = FaceDetector()
    video_capture = cv2.VideoCapture(0)

    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--detector", required=True,
                    help="path to OpenCV's deep learning face detector")
    ap.add_argument("-m", "--embedding-model", required=True,
                    help="path to OpenCV's deep learning face embedding model")
    ap.add_argument("-r", "--recognizer", required=True,
                    help="path to model trained to recognize faces")
    ap.add_argument("-l", "--le", required=True,
                    help="path to label encoder")
    ap.add_argument("-c", "--confidence", type=float, default=0.5,
                    help="minimum probability to filter weak detections")
    args = vars(ap.parse_args())

    # load our serialized face detector from disk
    print("[INFO] loading face detector...")
    protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])
    modelPath = os.path.sep.join([args["detector"],
                                "res10_300x300_ssd_iter_140000.caffemodel"])
    detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

    # load our serialized face embedding model from disk
    print("[INFO] loading face recognizer...")
    embedder = cv2.dnn.readNetFromTorch(args["embedding_model"])

    # load the actual face recognition model along with the label encoder
    recognizer = pickle.loads(open(args["recognizer"], "rb").read())
    le = pickle.loads(open(args["le"], "rb").read())

    count = 0

    while True:

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #Gets the RGB numpy image and returns tuples
        bboxes = face_detector.predict(rgb_img)
        print(bboxes)

        cropped_images = crop_images(frame, bboxes)

        # The Bulk of the processing of the bulk images
        for crop,x,y,w,h,p in cropped_images:
            faceBlob = cv2.dnn.blobFromImage(crop, 1.0/255,(96, 96), (0,0,0), swapRB=True, crop=False)
            embedder.setInput(faceBlob)
            vec = embedder.forward()

            preds = recognizer.predict_proba(vec)[0]
            j = np.argmax(preds)
            proba = preds[j]
            name = le.classes_[j]

            color = (0, 0, 255)

            if (proba*100 > 90):
                text = "{}: {:.2f}%".format(name, proba * 100)
                cv2.putText(frame, text, (int(x - w/2), int(y - h/2 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
                color = (0,255,0)

            cv2.rectangle(frame, (int(x - w/2), int(y - h/2)),
                            (int(x + w/2), int(y + h/2)), color, 3)

        # ann_img = annotate_image(frame, bboxes)
        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
