import pyautogui
import time

im1 = pyautogui.screenshot()
im1.save("my_screenshot.png")
im2 = pyautogui.screenshot("my_screenshot2.png")

pyautogui.write(
    "Hello world!", interval=0.25
)  # Type with quarter-second pause in between each key.

pyautogui.press("Enter")
time.sleep(2)

pyautogui.alert(
    "This is alert box!"
)  # Type with quarter-second pause in between each key.
