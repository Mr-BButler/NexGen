# define function to print Grid N
def gridN():
  print(" * - - - - - - - * ")
  print(" * * - - - - - - * ")
  print(" * - * - - - - - * ")
  print(" * - - * - - - - * ")
  print(" * - - - * - - - * ")
  print(" * - - - - * - - * ")
  print(" * - - - - - * - * ")
  print(" * - - - - - - * * ")
  print(" * - - - - - - - * ")

# define function to print Grid E  
def gridE():
  print(" * * * * * * * * * ")
  print(" * - - - - - - - - ")
  print(" * - - - - - - - - ")
  print(" * - - - - - - - - ")
  print(" * * * * * - - - - ")
  print(" * - - - - - - - - ")
  print(" * - - - - - - - - ")
  print(" * - - - - - - - - ")
  print(" * * * * * * * * * ")

# define function to print Grid X
def gridX():
  print(" * - - - - - - - * ")
  print(" - * - - - - - * - ")
  print(" - - * - - - * - - ")
  print(" - - - * - * - - - ")
  print(" - - - - * - - - - ")
  print(" - - - * - * - - - ")
  print(" - - * - - - * - - ")
  print(" - * - - - - - * - ")
  print(" * - - - - - - - * ")

# define function to print Grid G
def gridG():
  print(" - - - - * - - - - ")
  print(" - - - * - * - - - ")
  print(" - - * - - - * - - ")
  print(" - * - - - - - - - ")
  print(" * - - - * * * * * ")
  print(" - * - - - - - * - ")
  print(" - - * - - - * - - ")
  print(" - - - * - * - - - ")
  print(" - - - - * - - - - ")

# define function to print the Grids for NEXGEN one after the other
def printGridsNEXGEN():
  gridN()
  print()
  gridE()
  print()
  gridX()
  print()
  gridG()
  print()
  gridE()
  print()
  gridN()

# call function
printGridsNEXGEN()