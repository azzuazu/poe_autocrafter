import pyautogui

p = pyautogui.locateOnScreen("./img/CoE_all_skill.png")
x, y = pyautogui.center(p)
pyautogui.click(x, y)