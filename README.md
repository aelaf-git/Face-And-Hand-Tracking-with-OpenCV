# Face & Hand Tracking (OpenCV Haar Cascades)

A real-time face and hand detection application using **OpenCV** and **Haar Cascades**.

## Description

This project uses pre-trained Haar Cascade classifiers to detect faces and hands from a webcam feed.

- **Face Detection**: Uses the standard `haarcascade_frontalface_default.xml`.
- **Hand Detection**: Uses a custom `haarcascade_hand.xml`.

## Features

- **Real-time Detection**: fast detection using lightweight Haar cascades.
- **Visual Feedback**: Draws bounding boxes around detected faces (Blue) and hands (Green).

## Prerequisites

- Python 3.7+
- A working webcam

## Installation

1. Clone the repository or download the source code.
2. Create and activate a virtual environment (Optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Important**: Ensure the XML files are in the same directory:
   - `haarcascade_frontalface_default.xml`
   - `haarcascade_hand.xml`

## Usage

1. Run the tracker script:

   ```bash
   python tracker.py
   ```

2. The application will open a window showing the webcam feed.

3. **Controls**:
   - Press **`q`** to exit the application.

## Dependencies

- `opencv-python`
