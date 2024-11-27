"""
purpose:print() function systax and usage 
 Escape sequences
  - Characters whose presence is felt,but they were not print
  \t -tab space
  \n- New line 
  \b - overwrites previous character
  r" - row string


"""

print("hello world python")
print("hello \tworld \tpython")
print("hello \tworld \npython")

print()

#  To ignore the escape sequences 
print("hello \tworld \\npython")
print(r"hello \tworld  \npython")

print("c:\my\newfolder")
print(r"c:\my\newfolder")
print()

# print(data ,sep=" ",end="\n")
print("hello") #default end="\n"
print("world")

print("hello",end="__")
print("world") #default end="\n"

print("hello","python",12321,end="\t")  #default end="\n"
print("world")#default end="\n"

print("hello","python",12321,end="\t", sep =";")  #default end="\n"
print("world")#default end="\n"