#1. Write a Python function to find the maximum of three numbers.
def find_maximum(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
maximum = find_maximum(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is: {maximum}.")
