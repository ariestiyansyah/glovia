import time
from adafruit_circuitplayground.express import cpx

# Measure 3-axis acceleration
# 0, 9, 0 = up
# -9, 0, 0 = right
# 9, 0, 0 = left

THRESHOLD_UP        = 5  
THRESHOLD_RIGHT     = -5   
THRESHOLD_LEFT      = 5 

LEFT_COLOR          = 0xFF0000
RIGHT_COLOR         = 0xFF0000
ANIM_DELAY          = 0.200

LEFT_TURN = (
  (0, 1, 2, 3, 4, 7),
)

RIGHT_TURN = (
  (0, 1, 2, 4, 5, 7, 8, 9),
)

def animate_glove(animation, color, delay=ANIM_DELAY):
    for frame in animation:
        cpx.pixels.fill(0)
        for pixel in frame:
            cpx.pixels[pixel] = color
        time.sleep(delay)

    cpx.pixels.fill(0)
    time.sleep(ANIM_DELAY)
    

# Loop forever
while True:
    # Check slide switch position
    if cpx.switch:
        # Get acceleration values
        X, Y, Z = cpx.acceleration
        # Check if glove is down or up
        if Z < THRESHOLD_UP:
            # Determine glove orienation and animate
            if X < THRESHOLD_RIGHT:
                animate_glove(RIGHT_TURN, RIGHT_COLOR)
            elif Y > THRESHOLD_LEFT:
                animate_glove(LEFT_TURN, LEFT_COLOR)
