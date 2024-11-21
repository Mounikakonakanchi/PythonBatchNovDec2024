"""
Purpose:print() function  systax and usage 

"""
name ="Almight" #str

print("name=",name)

print("Name of Student is" +name)
print("Name of student is" +name)
print()

print("name of student is",name)
print("name of student is",name,sep=" ")
print(1,2,3,4,5,6,sep="-")
print(1,2,3,4,5,6,sep="")
print()

print(1,2,3,4,5,6) # default sep=''
print(1,2,3,4,5,6,sep="~")
print(1,2,3,4,5,6,sep="_")
print()

#Note: python is dynamic typed language 
name=1232
print("Name of the student is",name)

#            str            int
#print("Name of student is"+name)
#Typeerror:can only concatinate str(not"int")to str

#Note:Python is a dynamaicly typed language