# prints input-styled X-Grid using functions and global variables
s1 = " " + input("Enter symbol 1: ")
s2 = " " + input("Enter symbol 2: ")

line1 = s1 + s2 + s2 + s2 + s2 + s2 + s2 + s2 + s1
line2 = s2 + s1 + s2 + s2 + s2 + s2 + s2 + s1 + s2
line3 = s2 + s2 + s1 + s2 + s2 + s2 + s1 + s2 + s2
line4 = s2 + s2 + s2 + s1 + s2 + s1 + s2 + s2 + s2
line5 = s2 + s2 + s2 + s2 + s1 + s2 + s2 + s2 + s2 

# define functions
def gridXstyled():
  print(line1)
  print(line2)
  print(line3)
  print(line4)
  print(line5)
  print(line4)
  print(line3)
  print(line2)
  print(line1)

def gridOstyled():
  print(line5)
  print(line4)
  print(line3)
  print(line2)
  print(line1)
  print(line2)
  print(line3)
  print(line4)
  print(line5)

# call functions
gridXstyled()
print()
gridOstyled()
print()