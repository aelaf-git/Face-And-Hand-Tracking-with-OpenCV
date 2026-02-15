# Face & Hand Tracking (MediaPipe)

A real-time "smart" face and hand tracking application using **MediaPipe** and **OpenCV**.

## Description

This project utilizes [MediaPipe Holistic](https://google.github.io/mediapipe/solutions/holistic.html) to detect and track:

- **Face Mesh**: 468 landmarks on the face.
- **Hands**: 21 landmarks per hand (fingers and joints).

Unlike simple bounding boxes, this model understands the **geometry and pose** of your face and hands.

## Features

- **Holistic Tracking**: Simultaneously tracks face, pose, and hands.
- **Real-time Performance**: Optimized with FPS counter.
- **Mirror Mode**: Video feed is mirrored for natural interaction.
- **Skeletal Visualization**: Draws connections between joints.

## Prerequisites

- Python 3.7+
- A working webcam

## Installation

1. Clone the repository or download the source code.
2. Create and activate a virtual environment (Recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your virtual environment is activated:

   ```bash
   source venv/bin/activate
   ```

2. Run the tracker script:

   ```bash
   python tracker.py
   ```

3. **Controls**:
   - Press **`q`** to exit the application.

## Dependencies

- `opencv-python`
- `mediapipe`
