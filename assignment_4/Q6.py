# Q6. Write a Python function to check whether a number falls within a given range.

def check_range(num, lower, upper):
    if lower <=num <= upper:
        return True
    else:
        return False
    
number = float(input("Enter a number: "))
lower_bound = float(input("Enter the lower bound of the range: "))
upper_bound = float(input("Enter the upper bound of the range: "))

if check_range(number, lower_bound, upper_bound):
    print(f"{number} is within the range [{lower_bound}, {upper_bound}]")
else:
    print(f"{number} is not within the range [{lower_bound}, {upper_bound}]")