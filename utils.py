import cv2
import os

def load_cascades():
    base_path = os.path.join(os.path.dirname(__file__), "haarcascades")
    face_cascade = cv2.CascadeClassifier(os.path.join(base_path, "haarcascade_frontalface_default.xml"))
    eye_cascade = cv2.CascadeClassifier(os.path.join(base_path, "haarcascade_eye.xml"))
    return face_cascade, eye_cascade

