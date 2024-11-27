""""

Purpose: python is a dynamic typed  language 
    Programing Languages 
         - Classification
             1. Static -Type Languages
               - First declare the variable ,& then use it
                  int a, float b #Declaration 
                                 #Initialization

             2. Dynamic Type Languages
                 - Create when you need no declaration
                   num1=123
                 - Line by Line or Block based execution.

   Python Code -> Python byte code -> PythonInterpreter-> C compiler -> Machine 

   So,Python Is slower when compared to compiler based languages.

"""
num= 100
type(num)

print(type(num))

print(num)
print("num")

print("num1",num)
print("num1=",num)
print("num1=",num,"type=",type(num))

# works in both static and dynamic typing
num1=300
print("num1=",num1,"type=",type(num1))#int

# Python is a dynamic-typed language
num1=300.0
print("num1=",num1,"type=",type(num1))#float

num1=300.
print("num1=",num1,"type=",type(num1))#float

num1=300
print("num1=",num1,"type=",type(num1))#Tuple

num1=(300,)
print("num1=",num1,"type=",type(num1))#Tuple

num1="300"
print("num1=",num1,"type=",type(num1))#str

num1="three"
print("num1=",num1,"type=",type(num1))#str

num1=True
# num1 = true # Python is a case senstive language
print("num1=",num1,"type=",type(num1))#Boolean

num1=False
print("num1=",num1,"type=",type(num1))#Boolean

num1 =None
print("num1=",num1,"type=",type(num1))#none

num1="NONE"
print("num1=",num1,"type=",type(num1))#str

num1="none"
print("num1=",num1,"type=",type(num1))#str

# NOTE : Srtings need to declared in quotes