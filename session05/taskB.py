import time # used for delay
import styledGrids

# main function
def animationInputStyled():
  forever = True
  t = 0.25

# inputting the different styles
  style1 = input("Enter symbol 1: ")
  style2 = input("Enter symbol 2: ")
  style3 = input("Enter symbol 3: ")
  style4 = input("Enter symbol 4: ")
  
  while (forever):
    clearScreen()
    styledGrids.printXstyled(style1, style2)
    time.sleep(t)
    clearScreen()
    styledGrids.printXstyled(style1, style3)
    time.sleep(t)
    clearScreen()
    styledGrids.printXstyled(style4, style3)
    time.sleep(t)
    clearScreen()
    styledGrids.printXstyled(style4, style1)
    time.sleep(t)