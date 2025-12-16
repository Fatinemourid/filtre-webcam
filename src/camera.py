import cv2

def start_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Caméra non accessible")
    return cap
