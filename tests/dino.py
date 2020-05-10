import pyautogui
from PIL import Image, ImageGrab
import time

def screenshor():
    img = ImageGrab.grab().convert('L')
    return img

def press(key):
    pyautogui.keyDown(key)
    return

def detect(data):
    for i in range(485,525):
        for j in range (220,260):
            if data[i,j]< 100:
                press('up')
                return

press('up')
time.sleep(2)
while True:
    img = screenshor()
    data = img.load()
    detect(data)