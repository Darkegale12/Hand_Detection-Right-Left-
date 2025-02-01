import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)


cap = cv2.VideoCapture(0)  # Use 0 for the default camera

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Flip the frame horizontally for a mirror-like view
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(rgb_frame)

   
    if results.multi_handedness and results.multi_hand_landmarks:
        for idx, hand_handedness in enumerate(results.multi_handedness):
          
            label = hand_handedness.classification[0].label 

           
            hand_landmarks = results.multi_hand_landmarks[idx]

            
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Display which hand is detected
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            cv2.putText(
                frame,
                f"{label} Hand",
                (int(wrist.x * frame.shape[1]), int(wrist.y * frame.shape[0])),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )

    # Show the frame
    cv2.imshow("Hand Detection", frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
