import pyautogui as pag
import random
import time


while True:
  try:
    x = random.randint(50,150)
    y = random.randint(50,150)
    pag.moveTo(x, y, 0.5)
    time.sleep(2)
    pag.PAUSE = 2.5
    pag.FAILSAFE = True
  except:
    print("Lol")