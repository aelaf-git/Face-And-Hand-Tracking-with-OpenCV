import cv2
import mediapipe as mp

# 1. Initialize MediaPipe Holistic and Drawing utilities
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils
holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 2. Access the Webcam
# '0' is usually the default laptop cam. Use '1' or '2' for external USB cams.
cap = cv2.VideoCapture(0)

print("Press 'q' to exit the application.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Prepare image for MediaPipe
    # OpenCV uses BGR, but MediaPipe requires RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False # Performance optimization
    
    # 4. Perform Tracking
    results = holistic.process(image)

    # 5. Draw Results back on the frame
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # Convert back to BGR for display

    # Draw Face Landmarks
    if results.face_landmarks:
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,
                                 mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                 mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1))

    # Draw Right Hand
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    # Draw Left Hand
    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    # 6. Display the Output
    cv2.imshow('Hand and Face Tracking', image)

    # Break loop on 'q' key press
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()