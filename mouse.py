import pyautogui as pag
import random

def mouse():
  while True:
      try:
        print("mouse run")
        x = random.randint(0, 3840)
        y = random.randint(0,2160)
        pag.moveTo(x, y, 0.1)
        pag.FAILSAFE = True
      except:
         pass