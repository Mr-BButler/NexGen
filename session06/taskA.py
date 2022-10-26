import os
import time
from session04 import grids

def clearScreen():
  os.system('clear')

def animation1():
 
  delay = 1

  clearScreen()
  grids.printN()
  time.sleep(delay)
  clearScreen()
  grids.printE()
  time.sleep(delay)
  clearScreen()
  grids.printX()
  time.sleep(delay)

# run the code
animation1()