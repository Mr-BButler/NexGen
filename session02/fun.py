# Question 2 X-Grid using 2 different symbols & strings
n1 = " " + input("Enter Number 1: ")
n2 = " " + input("Enter Number 2: ")
#change string to integer
s1 = int(n1)
s2 = int(n2)


line1 = chr(s1) + chr(s2) + chr(s2) + chr(s2) + chr(s2) + chr(s2) + chr(s2) + chr(s2) + chr(s1)
line2 = chr(s2) + chr(s1) + chr(s2) + chr(s2) + chr(s2) + chr(s2) + chr(s2) + chr(s1) + chr(s2)
line3 = chr(s2) + chr(s2) + chr(s1) + chr(s2) + chr(s2) + chr(s2) + chr(s1) + chr(s2) + chr(s2)
line4 = chr(s2) + chr(s2) + chr(s2) + chr(s1) + chr(s2) + chr(s1) + chr(s2) + chr(s2) + chr(s2)
line5 = chr(s2) + chr(s2) + chr(s2) + chr(s2) + chr(s1) + chr(s2) + chr(s2) + chr(s2) + chr(s2)

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line4)
print(line3)
print(line2)
print(line1)