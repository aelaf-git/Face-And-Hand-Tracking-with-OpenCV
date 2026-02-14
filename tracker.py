import cv2
import time

class FaceHandTracker:
    def __init__(self, face_cascade_path='haarcascade_frontalface_default.xml', hand_cascade_path='haarcascade_hand.xml'):
        # Load classifiers with error handling
        self.face_cascade = cv2.CascadeClassifier(face_cascade_path)
        if self.face_cascade.empty():
            print(f"Error: Could not load '{face_cascade_path}'. Check if the file exists.")
        
        self.hand_cascade = cv2.CascadeClassifier(hand_cascade_path)
        if self.hand_cascade.empty():
            print(f"Warning: Could not load '{hand_cascade_path}'. Hand detection will be skipped.")
        
        # Initialize video capture
        self.cap = cv2.VideoCapture(0)
        
        # FPS calculation variables
        self.prev_time = 0
        self.curr_time = 0

    def detect_and_draw(self, frame, gray):
        """Perform detection and draw bounding boxes."""
        
        # 1. Detect Faces
        if not self.face_cascade.empty():
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # 2. Detect Hands
        if not self.hand_cascade.empty():
            hands = self.hand_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "Hand", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return frame

    def run(self):
        """Main loop for video capture and processing."""
        print("Press 'q' to exit.")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Mirror the frame naturally
            frame = cv2.flip(frame, 1)

            # Convert to grayscale for detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Process frame
            frame = self.detect_and_draw(frame, gray)

            # Calculate and display FPS
            self.curr_time = time.time()
            fps = 1 / (self.curr_time - self.prev_time)
            self.prev_time = self.curr_time
            cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Display result
            cv2.imshow('OpenCV Face & Hand Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    tracker = FaceHandTracker()
    tracker.run()