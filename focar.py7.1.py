from machine import Pin, PWM
from time import sleep

# Motor pins
E1 = PWM(Pin(28))
M1 = Pin(27, Pin.OUT)

E2 = PWM(Pin(26))
M2 = Pin(22, Pin.OUT)

# Motor PWM frequency
E1.freq(1000)
E2.freq(1000)

SPEED = 32767  # Approximately 50% PWM duty


def motor_left(direction, speed=SPEED):
    if direction == "forward":
        M1.value(1)
    elif direction == "backward":
        M1.value(0)
    else:
        E1.duty_u16(0)
        return

    E1.duty_u16(speed)


def motor_right(direction, speed=SPEED):
    if direction == "forward":
        M2.value(1)
    elif direction == "backward":
        M2.value(0)
    else:
        E2.duty_u16(0)
        return

    E2.duty_u16(speed)


def forward(speed=SPEED):
    motor_left("forward", speed)
    motor_right("forward", speed)


def backward(speed=SPEED):
    motor_left("backward", speed)
    motor_right("backward", speed)


def turn_left(speed=SPEED):
    motor_left("backward", speed)
    motor_right("forward", speed)


def turn_right(speed=SPEED):
    motor_left("forward", speed)
    motor_right("backward", speed)


def stop():
    E1.duty_u16(0)
    E2.duty_u16(0)


def led_on():
    Pin("LED", Pin.OUT).value(1)


def led_off():
    Pin("LED", Pin.OUT).value(0)