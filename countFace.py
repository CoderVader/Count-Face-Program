import cv2
import numpy as np
import dlib

# (0) denotes the primary camera of the laptop
image_capture = cv2.VideoCapture(0)

# dlib module to get coordinates
face_detector = dlib.get_frontal_face_detector()

while True:
    # Capturing the frames one at a time
    ret, frame = image_capture.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)

    face_count = 0

    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()

        cv2.rectangle(frame, (x,y), (x1, y1), (0, 255, 0), 2)

        face_count += 1

        cv2.putText(frame, 'Face Number: ' + str(face_count), (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        print(face, face_count)

    # Display the image

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Stop the face capture
    image_capture.release()

    # Close the windows
    cv2.destroyAllWindows()



