import face_recognition
import cv2
import numpy as np
import os

# Load known faces
known_face_encodings = []
known_face_names = []

print("🔍 Loading known faces...")
for filename in os.listdir("known_faces"):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = face_recognition.load_image_file(f"known_faces/{filename}")
        encodings = face_recognition.face_encodings(img)
        if encodings:
            known_face_encodings.append(encodings[0])
            known_face_names.append(os.path.splitext(filename)[0])
        else:
            print(f" No face found in {filename}")

# Start webcam
video_capture = cv2.VideoCapture(0)
print("📷 Camera started. Press Q to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print(" Failed to grab frame.")
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Find face locations and encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame)

    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        face_names.append(name)

    # Draw results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw rectangle and label
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 0, 0), 1)

    # Show the frame
    cv2.imshow('Face Recognition', frame)

    # Exit on Q key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()
