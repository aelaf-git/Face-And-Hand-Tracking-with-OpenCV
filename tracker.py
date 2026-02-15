import cv2
import mediapipe as mp
import time
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class FaceHandTracker:
    def __init__(self):
        # Initialize Face Landmarker
        base_options_face = python.BaseOptions(model_asset_path='face_landmarker.task')
        options_face = vision.FaceLandmarkerOptions(
            base_options=base_options_face,
            num_faces=1,
            min_face_detection_confidence=0.5,
            min_face_presence_confidence=0.5,
            min_tracking_confidence=0.5,
            output_face_blendshapes=False,
            output_facial_transformation_matrixes=False,
            running_mode=vision.RunningMode.VIDEO)
        self.face_landmarker = vision.FaceLandmarker.create_from_options(options_face)

        # Initialize Hand Landmarker
        base_options_hand = python.BaseOptions(model_asset_path='hand_landmarker.task')
        options_hand = vision.HandLandmarkerOptions(
            base_options=base_options_hand,
            num_hands=2,
            min_hand_detection_confidence=0.5,
            min_hand_presence_confidence=0.5,
            min_tracking_confidence=0.5,
            running_mode=vision.RunningMode.VIDEO)
        self.hand_landmarker = vision.HandLandmarker.create_from_options(options_hand)

        # Initialize video capture
        self.cap = cv2.VideoCapture(0)
        
        # FPS calculation variables
        self.prev_time = 0
        self.curr_time = 0

    def run(self):
        print("Press 'q' to exit.")
        
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            # Mirror the frame
            frame = cv2.flip(frame, 1)
            
            # Convert to RGB for MediaPipe
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)
            
            # Timestamp for video mode
            timestamp_ms = int(time.time() * 1000)
            
            # Detect
            face_result = self.face_landmarker.detect_for_video(mp_image, timestamp_ms)
            hand_result = self.hand_landmarker.detect_for_video(mp_image, timestamp_ms)
            
            # Visualization
            # Draw Face Points
            if face_result.face_landmarks:
                for face_landmarks in face_result.face_landmarks:
                    for landmark in face_landmarks:
                        x = int(landmark.x * frame.shape[1])
                        y = int(landmark.y * frame.shape[0])
                        cv2.circle(frame, (x, y), 1, (0, 255, 255), -1)

            # Draw Hand Points and Lines
            if hand_result.hand_landmarks:
                for hand_landmarks in hand_result.hand_landmarks:
                    # Draw points
                    h, w, _ = frame.shape
                    landmarks_px = [(int(l.x * w), int(l.y * h)) for l in hand_landmarks]
                    
                    for pt in landmarks_px:
                        cv2.circle(frame, pt, 3, (0, 255, 0), -1)
                        
                    # Draw simple connections (manual implementation of hand skeleton)
                    # Thumb
                    cv2.line(frame, landmarks_px[0], landmarks_px[1], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[1], landmarks_px[2], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[2], landmarks_px[3], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[3], landmarks_px[4], (0, 255, 0), 2)
                    # Index
                    cv2.line(frame, landmarks_px[0], landmarks_px[5], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[5], landmarks_px[6], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[6], landmarks_px[7], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[7], landmarks_px[8], (0, 255, 0), 2)
                    # Middle
                    cv2.line(frame, landmarks_px[9], landmarks_px[10], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[10], landmarks_px[11], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[11], landmarks_px[12], (0, 255, 0), 2)
                    # Ring
                    cv2.line(frame, landmarks_px[13], landmarks_px[14], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[14], landmarks_px[15], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[15], landmarks_px[16], (0, 255, 0), 2)
                    # Pinky
                    cv2.line(frame, landmarks_px[0], landmarks_px[17], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[17], landmarks_px[18], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[18], landmarks_px[19], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[19], landmarks_px[20], (0, 255, 0), 2)
                    # Palm
                    cv2.line(frame, landmarks_px[5], landmarks_px[9], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[9], landmarks_px[13], (0, 255, 0), 2)
                    cv2.line(frame, landmarks_px[13], landmarks_px[17], (0, 255, 0), 2)


            # Calculate and display FPS
            self.curr_time = time.time()
            if self.curr_time - self.prev_time > 0:
                fps = 1 / (self.curr_time - self.prev_time)
            else:
                fps = 0
            self.prev_time = self.curr_time
            cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Display result
            cv2.imshow('MediaPipe Face & Hand Tasks', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    tracker = FaceHandTracker()
    tracker.run()