# lets make a calculator

def addition(a,b): #this function is used for addition
    return a+b

def subtraction(a,b): #this function is used to subtraction
    return a-b

def multiplication(a,b):   #this function is used to multiple the given data
    return a*b

def division(a,b): #this function is used to perform devision
    return a/b


#lets take an input from user

a=float(input("Enter the main number : "))
b=float(input("Enter the secondary data:"))
c=input("Enter the symbol the operation that you want to perform:(EX:*,+,-,/) ")
if c=="+":
   print(f"The addition of given data is: {addition(a,b)}") 
elif c=="-":
    print(f"The subtraction of given data is: {subtraction(a,b)}")
elif c=="*":
    print(f"The multiplication  of given data is: {multiplication(a,b)}")
elif c=="/":
    print(f"The division of given data is: {division(a,b)}")
else:
    print("Invalid opperation")



