import pyautogui
import time
from rationals import rationals

time.sleep(10)

r = (0,1)
while True:
    
    time.sleep(1)

    r_next = rationals(r)
    r = r_next
    (x,y) = (r_next)
    pyautogui.press(str(x))
    pyautogui.press('/')
    pyautogui.press(str(y))
    pyautogui.press('return')
    
    time.sleep(1.5)

    pyautogui.keyDown("command")
    pyautogui.press("a")
    pyautogui.keyUp("command")
    pyautogui.press('delete')
