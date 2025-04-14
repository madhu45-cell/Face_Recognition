# **Face Recognition System**

## **Overview**

The **Face Recognition System** is a real-time application that leverages the **Face Recognition** library and **OpenCV** to detect and identify faces captured by a webcam. It compares the faces detected in the live video feed with known faces stored in a local directory, labeling each face with the corresponding name. This project is designed to demonstrate the capabilities of face recognition technology in a simple and intuitive manner.

## **Features**

- **Real-Time Face Recognition**: Identifies and labels faces detected by the webcam.
- **Customizable Known Faces**: Allows users to add known faces by placing image files in a specific directory.
- **Webcam Integration**: Captures live video from the webcam and processes each frame for face detection.
- **User-Friendly**: Automatically recognizes faces and displays the corresponding name. Unknown faces are marked as "Unknown."
- **Exit on Demand**: Press `Q` to close the application.

## **Technologies Used**

- **Python**: The primary programming language used for this project.
- **Face Recognition Library**: Provides a simple way to recognize faces.
- **OpenCV**: Used for handling webcam video capture and image processing.
- **NumPy**: A core library used for handling arrays and mathematical operations.

## **Installation**

Follow these steps to set up the project locally:

### 1. Clone the repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/your-username/face-recognition.git
cd face-recognition
