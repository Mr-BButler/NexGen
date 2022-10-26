import os
import time
from session04 import grids

delay = 1


def clearScreen():
  os.system('clear')

def animation1():
 
  

  clearScreen()
  grids.printN()
  time.sleep(delay)
  clearScreen()
  grids.printE()
  time.sleep(delay)
  clearScreen()
  grids.printX()
  time.sleep(delay)



# NEXGEN-Animation, 2 repetitions
def animation3() :
  
  delay = 1
  
for x in range(2) : # range(5) for 5 repetitions
    clearScreen()
    grids.printN()
    time.sleep(delay)
    clearScreen()
    grids.printE()
    time.sleep(delay)
    clearScreen()
    grids.printX()
    time.sleep(delay)
    clearScreen()
    grids.printG()
    time.sleep(delay)
    clearScreen()
    grids.printE()
    time.sleep(delay)
    clearScreen()
    grids.printN()
    time.sleep(delay)




# NEXGEN-Animation, infinite repetitions, twice as fast
def animation2():
  forever = True
  delay = 0.5 # delay = 2 for a slower animation
  

  while (forever):
    clearScreen()
    grids.printN()
    time.sleep(delay)
    clearScreen()
    grids.printE()
    time.sleep(delay)
    clearScreen()
    grids.printX()
    time.sleep(delay)
    clearScreen()
    grids.printG()
    time.sleep(delay)
    clearScreen()
    grids.printE()
    time.sleep(delay)
    clearScreen()
    grids.printN()
    time.sleep(delay)


# run the code
animation1()

# call function
animation3()
    
# call function
animation2()

