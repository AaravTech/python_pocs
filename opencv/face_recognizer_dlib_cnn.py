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

hardik_image = face_recognition.load_image_file("hardik.jpg")
hardik_face_encoding = face_recognition.face_encodings(hardik_image)[0]

nirav_image = face_recognition.load_image_file("nirav.jpeg")
nirav_face_encoding = face_recognition.face_encodings(nirav_image)[0]

keyur_image = face_recognition.load_image_file("keyur.jpg")
keyur_face_encoding = face_recognition.face_encodings(keyur_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    hardik_face_encoding,
    nirav_face_encoding,
    keyur_face_encoding
]
known_face_names = [
    "Hardik Patel",
    "Nirav Patel",
    "Keyur Rathod"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
num_jitters = 1

detector = dlib.get_frontal_face_detector() # Face detector
predictor_68_point_model = face_recognition_models.pose_predictor_model_location()
pose_predictor = dlib.shape_predictor(predictor_68_point_model) # Landmark detector

face_recognition_model = face_recognition_models.face_recognition_model_location()
face_encoder = dlib.face_recognition_model_v1(face_recognition_model) # Face encoder
SKIPP_FRAMES = 3
i = SKIPP_FRAMES
while True:
    ret, frame = video_capture.read()


    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = list(detector(rgb_small_frame, 1))
        landmarks_68 = [pose_predictor(rgb_small_frame, face_location) for face_location in face_locations]

        face_encodings = [np.array(face_encoder.compute_face_descriptor(rgb_small_frame, raw_landmark_set, num_jitters)) for raw_landmark_set in landmarks_68]

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.4)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

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