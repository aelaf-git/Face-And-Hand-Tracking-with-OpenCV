import cv2

# 1. Load the pre-trained classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("Error: Could not load 'haarcascade_frontalface_default.xml'. Check if the file exists.")

# Note: Pure OpenCV hand detection is less 'plug-and-play' than MediaPipe.
hand_cascade = cv2.CascadeClassifier('haarcascade_hand.xml') 
if hand_cascade.empty():
    print("Warning: Could not load 'haarcascade_hand.xml'. Hand detection will be skipped.")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale (required for Haar Cascades)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Detect Faces
    if not face_cascade.empty():
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # 3. Detect Hands
    if not hand_cascade.empty():
        # This cascade is famously 'noisy' compared to AI models
        hands = hand_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in hands:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Hand", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('OpenCV Face & Hand Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()