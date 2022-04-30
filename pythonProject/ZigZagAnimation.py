import sys
import time


def draw(num):
    print(" " * num + "********")


try:
    while True:
        for x in range(5):
            draw(x)
            time.sleep(.1)
        for x in range(5, 0, -1):
            draw(x)
            time.sleep(.1)
except KeyboardInterrupt:
    sys.exit()
