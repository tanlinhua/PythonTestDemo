import time
import pyautogui

text = "I Love You!"

time.sleep(3)

while True:
    pyautogui.typewrite(text, 0.05)
    pyautogui.press("enter")
    time.sleep(0.5)
