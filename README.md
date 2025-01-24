**SRS (Software Requirements Specification)** 

---

### **1. Introduction**
#### 1.1 Purpose
The Virtual Try-On System allows users to try on virtual clothes by overlaying shirt images on their live video feed. It uses OpenCV for image processing and face detection to accurately place shirts on the user's body.

#### 1.2 Scope
The system overlays shirt images onto a user's body based on detected faces in real-time from a webcam. The system provides an interactive user interface to show the virtual try-on experience.

#### 1.3 Definitions, Acronyms, and Abbreviations
- **OpenCV**: Open Source Computer Vision Library.
- **Webcam**: A device for capturing live video.
- **Haar Cascade**: A machine learning object detection method used in OpenCV for detecting objects (such as faces).
- **Overlay**: Placing an image (shirt) on top of another image (live video frame).

#### 1.4 References
- OpenCV documentation: https://opencv.org/
- GitHub repository for the project: [Link to GitHub repo]

---

### **2. Overall Description**
#### 2.1 Product Perspective
This system is designed for a standalone desktop application that uses a webcam for capturing video and overlays a shirt image onto the user's body based on face detection. It does not require an internet connection and functions locally.

#### 2.2 Product Features
- Real-time face detection using Haar Cascade.
- Ability to overlay a shirt image onto a detected face.
- Adjustable shirt size based on the user's body.
- Interactive and real-time virtual try-on experience.

#### 2.3 User Classes and Characteristics
- **End Users**: Anyone with a webcam who wants to try virtual clothing.
- **Developers**: Responsible for maintaining and updating the system.

#### 2.4 Operating Environment
- Windows 10 or later
- Python 3.7 or higher
- OpenCV 4.x or higher

#### 2.5 Constraints
- Requires a webcam to capture live video.
- Limited to the size of the shirt image being used.
- Real-time performance may be affected by low system specifications.

#### 2.6 Assumptions and Dependencies
- The system assumes the user is facing the camera directly.
- The system depends on the availability of a compatible webcam.
- OpenCV library must be installed for image processing.

---

### **3. Functional Requirements**
#### 3.1 Face Detection
- **Description**: The system must detect faces from the live video feed using OpenCV's Haar Cascade face detection algorithm.
- **Inputs**: Video frame from the webcam.
- **Outputs**: Bounding box coordinates for detected faces.

#### 3.2 Image Overlay
- **Description**: Once a face is detected, the system must resize the shirt image to fit the detected face and overlay it onto the video frame.
- **Inputs**: Shirt image, face bounding box coordinates.
- **Outputs**: The video frame with the shirt image overlaid on the detected face.

#### 3.3 Webcam Feed
- **Description**: The system must display the live webcam feed in a window.
- **Inputs**: Live video stream from the webcam.
- **Outputs**: A window showing the video with the overlay applied.

#### 3.4 User Interaction
- **Description**: The user should be able to stop the video feed by pressing the 'q' key.
- **Inputs**: Keyboard input ('q' to quit).
- **Outputs**: Closes the video feed window and terminates the application.

---

### **4. Non-Functional Requirements**
#### 4.1 Performance Requirements
- The system should process at least 15 frames per second (FPS) to ensure real-time overlay.
- The overlay should be applied within 200 milliseconds of detecting the face.

#### 4.2 Usability Requirements
- The system should provide real-time feedback, meaning the overlay should appear as soon as the face is detected.
- The interface should be simple, with the primary action being the webcam feed showing the virtual try-on.

#### 4.3 Security Requirements
- There are no explicit security concerns, but the system should handle errors gracefully if a webcam is not available.

#### 4.4 Reliability
- The system should not crash when no face is detected, and it should continue to run as long as the webcam feed is active.

#### 4.5 Maintainability
- The code should be modular, with separate functions for face detection, image resizing, and overlay logic.
- The system should be easy to extend for adding more clothing items or enhancing the detection accuracy.

#### 4.6 Compatibility
- The system should be compatible with Windows, macOS, and Linux, as long as OpenCV is supported.

---

### **5. System Models**
#### 5.1 Use Case Diagram
The system involves the following use case:
1. **Start Webcam Feed**: Start the video feed and detect faces in real-time.
2. **Overlay Shirt Image**: Resize and overlay the shirt image on the detected face.
3. **Stop the Application**: Exit the application when the user presses 'q'.

#### 5.2 Sequence Diagram
1. The **Webcam** sends frames to the system.
2. **Face Detection** processes the frame to detect faces.
3. If a face is detected, the **Shirt Image** is resized and overlaid.
4. The **Video Frame** with the shirt overlay is displayed.

---

### **6. External Interface Requirements**
#### 6.1 User Interface
- A simple window will display the webcam feed.
- The shirt will be shown over the detected face.

#### 6.2 Hardware Interface
- Webcam (integrated or external) to capture live video.

#### 6.3 Software Interface
- The system uses **OpenCV** to process images and handle video streams.
- The system is written in **Python 3** and uses the `cv2` library for computer vision tasks.

---

### **7. Appendices**
- **Appendix A**: GitHub repository for the project.
- **Appendix B**: OpenCV documentation for face detection and image processing.

---

