def printXstyled(s1, s2):
  #add blank to the symbols
  s1 = " " + s1
  s2 = " " + s2

  #defining lines that can be reused for the Grid X  
  line1 = s1 + s2 + s2 + s2 + s2 + s2 + s2 + s2 + s1
  line2 = s2 + s1 + s2 + s2 + s2 + s2 + s2 + s1 + s2
  line3 = s2 + s2 + s1 + s2 + s2 + s2 + s1 + s2 + s2
  line4 = s2 + s2 + s2 + s1 + s2 + s1 + s2 + s2 + s2
  line5 = s2 + s2 + s2 + s2 + s1 + s2 + s2 + s2 + s2

  #print lines
  print(line1)
  print(line2)
  print(line3)
  print(line4)
  print(line5)
  print(line4)
  print(line3)
  print(line2)
  print(line1)

# call function with example parameters
printXstyled("X", ".")
