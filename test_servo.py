from pyfirmata2 import Arduino
import time

# Initialize the board and servo pin
board = Arduino('COM11')  # Replace with your Arduino's COM port
servo_pin = 9  # Servo connected to pin 9

# Configure the servo pin
board.servo_config(servo_pin)

def test_servo():
    """Test the servo by rotating it continuously."""
    while True:
        for angle in range(0, 181, 10):  # Rotate from 0 to 180 degrees
            board.digital[servo_pin].write(angle)
            time.sleep(0.1)
        for angle in range(180, -1, -10):  # Rotate back from 180 to 0 degrees
            board.digital[servo_pin].write(angle)
            time.sleep(0.1)

if __name__ == "__main__":
    test_servo()