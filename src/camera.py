import cv2
from src.eye_detector import detect_eyes
from src.blink_detector import BlinkDetector
from src.morse_interpreter import MorseInterpreter
from src.tts import Speaker

blink_detector = BlinkDetector()
morse = MorseInterpreter()
speaker = Speaker()

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
                morse.add_signal(blink)

        morse.update()
        message = morse.get_message()

        cv2.putText(frame, message, (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        cv2.imshow("VisionMorse - Morse Interpreter", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if morse.is_word_completed():
            speaker.speak(morse.get_message())

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_camera()
