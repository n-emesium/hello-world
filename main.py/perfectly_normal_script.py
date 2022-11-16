from pynput.keyboard import Controller
keyboard = Controller()

from random import randint
from time import sleep


if __name__ == "__main__":
    while True:
        with keyboard.pressed(Key.shift):
            sleep(randint(2, 5))
        sleep(randint(2, 5))