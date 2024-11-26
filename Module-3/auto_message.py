import pyautogui
import time

for i in range(1, 25):
    time.sleep(3)
    pyautogui.write("Hello World!", interval=0.25)
    pyautogui.press("Enter")
