from time import sleep
import focar

# Adjust these times after testing your FoCar
FORWARD_TIME = 1.8
TURN_TIME = 0.6
PAUSE_TIME = 0.3

focar.stop()
focar.led_on()
sleep(1)

# Step 1: Move forward approximately one meter
focar.forward()
sleep(FORWARD_TIME)
focar.stop()
sleep(PAUSE_TIME)

# Step 2: Three-point turn - first movement
focar.forward()
sleep(TURN_TIME)
focar.stop()
sleep(PAUSE_TIME)

# Step 3: Three-point turn - reverse while turning
focar.backward()
sleep(TURN_TIME)
focar.stop()
sleep(PAUSE_TIME)

# Step 4: Turn forward to face the opposite direction
focar.forward()
sleep(TURN_TIME)
focar.stop()
sleep(PAUSE_TIME)

# Step 5: Return toward the starting point
focar.forward()
sleep(FORWARD_TIME)
focar.stop()

focar.led_off()
print("FoCar movement completed!")