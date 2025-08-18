import speech_recognition as sr
import webbrowser
import pyttsx3


recognitizer = sr.Recognizer()
engine = pyttsx3.init()

def speak (text):
    engine.say(text)
    engine.runAndWait()

if __name__ == " __main__ ":
    speak("hey sir how i may help you fuck")