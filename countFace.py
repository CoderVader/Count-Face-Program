import opencv
import numpy as np
import dlib

# (0) denotes the primary camera of the laptop
image_capture = cv2.VideoCapture(0)

# dlib module to get coordinates
face_detector = dlib.get_frontal_face_detector()

