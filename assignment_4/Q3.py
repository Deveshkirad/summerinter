#3. Write a Python function to multiply all the numbers in a list.


def multiply(list):
    result = 1
    for i in range(len(list)):
        result *= list[i]
    return result

#taking input from user as list using for loop
input_list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = float(input(f"Enter element {i+1}: "))
    input_list.append(element)

result = multiply(input_list)
print(f"The product of the elements in the list is: {result}")