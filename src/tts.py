import pyttsx3

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 160)
        self.engine.setProperty("volume", 1.0)
        self.last_spoken = ""

    def speak(self, text):
        if text and text != self.last_spoken:
            self.engine.say(text)
            self.engine.runAndWait()
            self.last_spoken = text
