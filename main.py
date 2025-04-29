from servo_control import move_servo
from voice_recognition import recognize_speech

if __name__ == "__main__":
    while True:
        command = recognize_speech()
        if command is None:
            print("No command detected. Please try again.")
            continue
        if command.lower() == "open":
            move_servo(90)  # Open position
        elif command.lower() == "close":
            move_servo(0)  # Close position
        else:
            print("Invalid command. Please say 'Open' or 'Close'.")