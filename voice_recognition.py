import sys
sys.stdout.reconfigure(encoding='utf-8')

import speech_recognition as sr

recognizer = sr.Recognizer()

def recognize_speech():
    """Nhận diện giọng nói và trả về lệnh."""
    with sr.Microphone() as source:
        print("Nói gì đó...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="vi-VN")
            print(f"Bạn nói: {command}")
            return command
        except sr.UnknownValueError:
            print("Không nhận diện được giọng nói.")
            return None