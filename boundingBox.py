import cv2
import sys
import logging as log
import datetime as dt
from time import sleep

from faced import FaceDetector
from faced.utils import annotate_image

def crop_images(frame, bboxes):
    image = frame[:]

    crop_img = img_h, img_w = frame.shape

    for x,y,w,h,p in bboxes:
        crop_img = frame[y:y+h, x:x+w]

    cv2.imshow("cropped", crop_img)
    pass

def main():
    #Initialize the Facial Recognition Neural Network
    face_detector = FaceDetector()

    video_capture = cv2.VideoCapture(0)
    anterior = 0

    while True:

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #Gets the RGB numpy image and returns tuples
        bboxes = face_detector.predict(rgb_img)
        print(bboxes)

        ann_img = annotate_image(frame, bboxes)
        # Display the resulting frame
        cv2.imshow('Video', ann_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
