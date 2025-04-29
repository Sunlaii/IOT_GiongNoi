import sys
sys.stdout.reconfigure(encoding='utf-8')

import speech_recognition as sr

recognizer = sr.Recognizer()

def recognize_speech():
    """Nhận diện giọng nói và trả về lệnh."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce noise from the environment
        print("Say something...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="en-US")
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Could not recognize speech.")
            return None