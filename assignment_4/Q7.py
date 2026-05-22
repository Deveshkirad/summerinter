#Q7. Write a Python function to Print Even Numbers from a Given List
def print_even_numbers(num_list):
    for num in num_list:
        if num % 2 == 0:
            print(num)
        
print("Enter the number of elements in the list:")
n = int(input())
numbers = []
print("Enter the numbers:")
for i in range(n):
    num = int(input())
    numbers.append(num)

print("Even numbers in the list:")
print_even_numbers(numbers)