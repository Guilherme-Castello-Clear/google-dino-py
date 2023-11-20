import time
import pyautogui
from PIL import ImageGrab, ImageOps
#831 416
x, y = pyautogui.position()
print(f'mouse: x={x}, y={y}')


def is_obstacle():
    box = (370, 437, 671, 482)
    image = ImageGrab.grab(box)
    image.save('a.png')
    gray_image = ImageOps.grayscale(image)
    for pixel in gray_image.getdata():
        if pixel < 100:
            print(pixel)
            return True
    return False


def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')
    time.sleep(1)


while True:
    if is_obstacle():
        jump()
    time.sleep(0.1)
