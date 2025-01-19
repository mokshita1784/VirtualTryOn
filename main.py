import cv2
import numpy as np

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the specific shirt image with an alpha channel
shirt_path = r'C:\Users\moksh\OneDrive\Desktop\Resources\Shirts\1.png'  # Path to the specific shirt image
shirt_image = cv2.imread(shirt_path, cv2.IMREAD_UNCHANGED)

# Check if the shirt image was loaded successfully
if shirt_image is None:
    print("Error: Shirt image not found.")
    exit()

# Function to overlay the shirt on the frame
def overlay_shirt(frame, shirt, face_rect):
    (x, y, w, h) = face_rect

    # Resize the shirt to match the face width and maintain aspect ratio
    shirt_width = w
    shirt_height = int(shirt.shape[0] * (shirt_width / shirt.shape[1]))
    shirt_resized = cv2.resize(shirt, (shirt_width, shirt_height), interpolation=cv2.INTER_AREA)

    # Calculate position to overlay the shirt
    y_offset = y + h
    x_offset = x

    # Ensure the shirt fits within the frame boundaries
    y1, y2 = max(0, y_offset), min(frame.shape[0], y_offset + shirt_resized.shape[0])
    x1, x2 = max(0, x_offset), min(frame.shape[1], x_offset + shirt_resized.shape[1])

    # Adjust shirt dimensions to fit the frame
    shirt_resized = shirt_resized[:y2 - y1, :x2 - x1]

    # Check if the shirt has an alpha channel; if not, add one
    if shirt_resized.shape[2] == 3:
        alpha_channel = np.ones((shirt_resized.shape[0], shirt_resized.shape[1], 1), dtype=np.uint8) * 255
        shirt_resized = np.concatenate((shirt_resized, alpha_channel), axis=2)

    # Blend the shirt image with the frame
    for c in range(3):  # Loop through BGR channels
        frame[y1:y2, x1:x2, c] = (
            shirt_resized[:, :, c] * (shirt_resized[:, :, 3] / 300.0) +  # Shirt pixel with alpha
            frame[y1:y2, x1:x2, c] * (1.0 - shirt_resized[:, :, 3] / 300.0)  # Frame pixel with inverse alpha
        )

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    # Overlay the shirt for each detected face
    for face_rect in faces:
        overlay_shirt(frame, shirt_image, face_rect)

    # Display the resulting frame
    cv2.imshow('Virtual Try-On', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()

