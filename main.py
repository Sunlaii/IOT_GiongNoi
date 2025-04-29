from servo_control import move_servo
from voice_recognition import recognize_speech

if __name__ == "__main__":
    while True:
        command = recognize_speech()
        if command == "trái":
            move_servo(0)
        elif command == "phải":
            move_servo(90)
        else:
            print("Lệnh không hợp lệ. Hãy nói 'trái' hoặc 'phải'.")