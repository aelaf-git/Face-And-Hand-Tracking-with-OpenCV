import cv2
import mediapipe as mp
import time

class FaceHandTracker:
    def __init__(self):
        # Initialize MediaPipe Holistic
        self.mp_holistic = mp.solutions.holistic
        self.mp_drawing = mp.solutions.drawing_utils
        self.holistic = self.mp_holistic.Holistic(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        # Initialize video capture
        self.cap = cv2.VideoCapture(0)
        
        # FPS calculation variables
        self.prev_time = 0
        self.curr_time = 0

    def detect_and_draw(self, frame):
        """Perform detection and draw landmarks."""
        
        # MediaPipe requires RGB, OpenCV uses BGR
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False # Improve performance
        
        # Process image
        results = self.holistic.process(image)
        
        # Convert back to BGR for drawing
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw Face Landmarks
        if results.face_landmarks:
            self.mp_drawing.draw_landmarks(
                image, 
                results.face_landmarks, 
                self.mp_holistic.FACEMESH_CONTOURS,
                self.mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                self.mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
            )

        # Draw Right Hand
        if results.right_hand_landmarks:
            self.mp_drawing.draw_landmarks(
                image, 
                results.right_hand_landmarks, 
                self.mp_holistic.HAND_CONNECTIONS
            )

        # Draw Left Hand
        if results.left_hand_landmarks:
            self.mp_drawing.draw_landmarks(
                image, 
                results.left_hand_landmarks, 
                self.mp_holistic.HAND_CONNECTIONS
            )
        
        return image

    def run(self):
        """Main loop for video capture and processing."""
        print("Press 'q' to exit.")
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            # Mirror the frame naturally
            frame = cv2.flip(frame, 1)

            # Process frame
            frame = self.detect_and_draw(frame)

            # Calculate and display FPS
            self.curr_time = time.time()
            fps = 1 / (self.curr_time - self.prev_time)
            self.prev_time = self.curr_time
            cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Display result
            cv2.imshow('MediaPipe Face & Hand Tracking', frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    tracker = FaceHandTracker()
    tracker.run()