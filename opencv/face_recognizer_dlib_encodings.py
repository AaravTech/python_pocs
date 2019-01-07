import face_recognition
import cv2
import dlib
import numpy as np
try:
    import face_recognition_models
except Exception:
    print("Please install `face_recognition_models` with this command before using `face_recognition`:\n")
    print("pip install git+https://github.com/ageitgey/face_recognition_models")
    quit()


video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
face_names = []

detector = dlib.get_frontal_face_detector()

process_this_frame = True
SKIPP_FRAMES = 3
i = SKIPP_FRAMES
while True:
    ret, frame = video_capture.read()


    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = list(detector(rgb_small_frame, 1))
        
        face_names = []
        for fl in face_locations:

            name = "Unknown"


            face_names.append(name)

    if i:
        process_this_frame = False
        i -= 1
    else:
        process_this_frame = True
        i = SKIPP_FRAMES

    for fl, name in zip(face_locations, face_names):
    # for fl in face_locations:
        top = fl.top() * 4
        right = fl.right() * 4
        bottom  = fl.bottom() * 4
        left = fl.left() * 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()