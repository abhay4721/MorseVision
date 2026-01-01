import cv2
from eye_detector import detect_eyes
from blink_detector import BlinkDetector

blink_detector = BlinkDetector()

def start_camera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame, left_eye, right_eye = detect_eyes(frame)

        if left_eye is not None and right_eye is not None:
            ear_left = blink_detector.eye_aspect_ratio(left_eye)
            ear_right = blink_detector.eye_aspect_ratio(right_eye)
            ear = (ear_left + ear_right) / 2

            blink = blink_detector.detect_blink(ear)
            if blink:
                print("Blink Detected:", blink)

        cv2.imshow("VisionMorse - Blink Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_camera()
