import time
import random
import pyautogui

time.sleep(3)

with open('spam.txt', 'r', encoding='u8') as f:
    lines = f.readlines()

# while True:
for _ in range(50):
    pyautogui.typewrite(random.choice(lines), 0.15)
    pyautogui.press("enter")
    time.sleep(random.randint(1, 3))
