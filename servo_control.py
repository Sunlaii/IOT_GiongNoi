from pyfirmata2 import Arduino
import time

board = Arduino('COM11')  # Thay COM11 bằng cổng Arduino của bạn
servo_pin = 9  # Chân 9 ở chế độ servo

def move_servo(angle):
    """Di chuyển servo đến góc chỉ định."""
    board.servo_config(servo_pin)
    board.digital[servo_pin].write(angle)  # Chuyển đổi góc trực tiếp cho servo
    time.sleep(1)