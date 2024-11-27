#!/usr/bin/python3
"""
purpose: Basic PEP 8 guidlines
      shebang line

  PEP - python enhancment  proposal
  PEP 8 - coding style guide

This is a doc string


"""

#print as a statement in python02
#print"Hello world!"

#print as a funtion in python 2&3
print("Hello wolrd!")
print(True)
print("True",123,None)

def wishes(name):
    wish="How are you{0}?".format(name)
    print(wish)

wishes("Mounika")