# Face & Hand Tracking (MediaPipe Tasks)

A real-time "smart" face and hand tracking application using the modern **MediaPipe Tasks API**.

## Description

This project uses the latest locally-run AI models to detect:

- **Face Landmarks**: 468 points on the face.
- **Hand Landmarks**: 21 skeletal points per hand.

It uses the `mediapipe.tasks.vision` API which is compatible with newer Python versions (3.13+).

## Features

- **Robust Tracking**: Uses `face_landmarker.task` and `hand_landmarker.task` models.
- **Real-time Performance**: Optimized loop with FPS counter.
- **Mirror Mode**: Video feed is flipped for natural interaction.
- **Custom Visualization**: Draws detailed skeletons and mesh points.

## Prerequisites

- Python 3.7+
- A working webcam

## Installation

1. Clone the repository or download the source code.
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Models**: The script requires `face_landmarker.task` and `hand_landmarker.task` in the project directory.

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
