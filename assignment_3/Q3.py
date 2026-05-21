#3) Write a program to check Palindrome Number

# For example Number 12321 is a Palindrome Number, because 12321 is equal to its reverse Number 12321.
#Steps for checking Palindrome number
#1. Find reverse of the given number.
#2. Compare that number with the reverse number.
#3. If number and its reverse is equal then it is a Palindrome Number otherwise not.


def is_palindrome(num): 
    # Convert the number to string to reverse it
    str_num = str(num)
    
    # Reverse the string
    reversed_str_num = str_num[::-1]
    
    # Check if the original string is equal to the reversed string
    if str_num == reversed_str_num:
        return True
    else:
        return False
    

number = int(input("Enter a number: "))

if is_palindrome(number):
    print(f"{number} is a Palindrome Number.")
else:
    print(f"{number} is not a Palindrome Number.")













