"""Face recognition from Image/all data."""
import face_recognition
# from io import StringIO

import os
import cv2
import csv

# import json
import numpy as np

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)
filepath = "face_recognitiontest.csv"
load = True
filewrite = open(filepath, "a", newline="")
fileread = open(filepath, newline="\n")
imagesos = []
# imagesos = os.listdir("/home/neo/Documents/Python/Images/all/")
images = []
for item in imagesos:
    images.append("/home/neo/Documents/Python/Images/all/" + item)
images.append("/home/neo/Documents/Python/Images/Yann.jpg")

known_face_encodings = []
known_face_names = []

csvwriter = csv.writer(
    filewrite, delimiter=","
)  # , quotechar='', quoting=csv.QUOTE_MINIMAL)
if load:
    # npdata = np.load('face_recognitiontest.npy', allow_pickle=True):
    try:
        with open("face_recognitiontestdb.csv", "r") as db:
            if os.fstat(db.fileno()).st_size:
                known_face_encodings = np.loadtxt(db, delimiter=",", skiprows=1,
                                                   unpack=True).tolist()
            else:
                print("Error db loading : File is empty")
                load = False
    except (StopIteration, UserWarning):
        load = False
    csvreader = csv.reader(fileread, delimiter=",")  # , quotechar='')
    csvlist = []
    for idlist, item in enumerate(csvreader):
        # known_face_encodings.append(npdata[idlist])
        # print(npdata[idlist])
        print(item[0])
        known_face_names.append(item[1])
        csvlist.append(item)
    fileread.close()

for item in images:
    try:
        # Load a sample picture and learn how to recognize it.
        print(item)
        item_image = face_recognition.load_image_file(item)
        item_face_encoding = face_recognition.face_encodings(item_image)[0]
        imgname = item.split("/")[-1]
        facename = imgname.split(".")[0]
        if load:
            if item not in csvlist[0]:
                print(csvlist[0])
                print("Append and save")
                known_face_encodings.append(item_face_encoding)
                known_face_names.append(facename)
                csvwriter.writerow([item, facename])
            else:
                print("No append")
        else:
            print("Append")
            known_face_encodings.append(item_face_encoding)
            known_face_names.append(facename)
            csvwriter.writerow([item, facename])
    except IsADirectoryError or ValueError:
        print("Error on " + item)
filewrite.close()
np.savetxt("face_recognitiontestdb.csv", known_face_encodings, delimiter=",")
print(known_face_encodings)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations
        )

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding
            )
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding
            )
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(
            frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED
        )
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow("Video", frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
