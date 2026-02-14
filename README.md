# FaceTracking

A real-time face and hand tracking application using [MediaPipe](https://github.com/google/mediapipe) and [OpenCV](https://opencv.org/).

## Description

This project utilizes MediaPipe's Holistic solution to detect and track face landmarks and hand poses (left and right) from a webcam feed. It visualizes the tracking results directly on the video stream in real-time.

## Features

- **Holistic Tracking**: Simultaneously tracks face mesh and hand landmarks.
- **Real-time Performance**: Optimized for fluid performance using MediaPipe's lightweight models.
- **Visual Feedback**: Draws landmarks and connections for:
  - Face Mesh (Contours)
  - Left Hand
  - Right Hand

## Prerequisites

- Python 3.7+
- A working webcam

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   _Note: It is recommended to use a virtual environment._

## Usage

1. Run the tracker script:

   ```bash
   python tracker.py
   ```

2. The application will open a window showing the webcam feed with tracking overlays.

3. **Controls**:
   - Press **`q`** to exit the application.

## Dependencies

- `opencv-python`
- `mediapipe`
