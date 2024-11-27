"""
purpose: Identifiers in python

   variable
      1.keyword   -> words which have meaning in the language 
      2.Identifier -> words which are defined by user or Developer

"""
# Loading a module 
import keyword

print(keyword.kwlist) 
# ['False', 'None', 'True', 'and', 'as', 'await', 'break', 
# 'assert', 'async', 'class', 'continue', 'def','del',
#  'elif', 'else', 'except', 'finally', 'for', 'from', 
# 'global', 'if', 'import', 'in', 'is', 'lambda', '
# nonlocal', 'not', 'or', 'pass', 'raise', 
# 'return', 'try', 'while', 'with', 'yield']

print(True)
#print(true)# Nameerror:name "true"is not defined

my_value='somthing'
print(my_value)#identifier

#True ="somthing"
#syntaxerror:cannot assign to true

print(keyword.iskeyword("True"))      #True
#print(ketword.iskeyword("true"))     #False
print(keyword.iskeyword("my_value"))  #False

#Identifier_user_defined variables 
    #Nameing converntion
#      1.keywords should not be used as identifiers
#      2.first character should be : a_z,A_Z,__
#      3.remaing character : a_z,A_Z,_,0_9

# ____Rule 1
# True =123 # syntaxerror: cannot assign to True
# None='Nothing'#syntaxerror:cannot assign to None

# PEP 8 - Dont create identifiers which are similar to 
true = 123
none ='Nothing'
  
true_value =123
none_result = "Nothing"

#___Rule 2&3
name = "Priyanka"
name_of_student = "priyanka"
first_name = "priyanka"
student_1 ="priyanka"
class_02_a = "python comment operations"
first__child = "satvik"

#PEP 8 recommnends to use capitals for constants
PI = 3.1416
DOZEN = 12

#$name = "priyanka"
#name-of-student = "priyanka"
name_of_student = "priyanka"

__end_student = "someone"
_job = "software development"
__role = "producation support"
__salary = 1231231223123

#opp->name mangling
#variable -> public variable 
#_variable -> protected variable
#__variable -> private variable 

#__variable__ ->built-in functions
#ex: __file__,__name__,__doc__,__init__,__dict__

print("__name__=",__name__)#__main__
print("__file__=",__file__)

#print("__lohith__=",__lohith__)
#namerror: name'__lohith__"is not difined