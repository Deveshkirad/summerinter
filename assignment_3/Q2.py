#Q 2) Write a function for basic math operations like add multiply substract divide and use this in your program, take 2 number input from user.

def add(a,b):
	return a+b  

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("Enter two numbers:")
num1=float(input())
num2=float(input())
print("Addition:",add(num1,num2))
print("Subtraction:",subtract(num1,num2))
print("Multiplication:",multiply(num1,num2))
print("Division:",divide(num1,num2))
 

