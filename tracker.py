import cv2
from collections import deque

# Load Haar Cascade models
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

# Start video capture
camera = cv2.VideoCapture(0)

# Global stats
attention_score = 0
status_text = "NOT ATTENTIVE"

# Keep history of last 30 frames
history = deque(maxlen=30)

def generate_frames():
    global attention_score, status_text
    while True:
        success, frame = camera.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        frame_score = 0

        if len(faces) > 0:
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]

                eyes = eye_cascade.detectMultiScale(roi_gray)

                # Draw rectangle around face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                if len(eyes) >= 1:
                    frame_score = 100
                else:
                    frame_score 
        else:
            frame_score = 0

        # Save this frame's score in history
        history.append(frame_score)
        attention_score = int(sum(history) / len(history))

        if attention_score > 70:
            status_text = "ATTENTIVE"
        elif attention_score > 30:
            status_text = "PARTIALLY ATTENTIVE"
        else:
            status_text = "NOT ATTENTIVE"

        # Encode frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def get_attention_stats():
    return {
        "score": attention_score,
        "status": status_text
    }




