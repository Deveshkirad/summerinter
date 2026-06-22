#1) Write a Python program to repeat a tuple three times using the * operator. 2) Write a Python program to join three separate tuples into one new tuple using the + operator. 3) Write a Python program to check whether a specific element exists inside a tuple using the in keyword. 4) Write a Python program to calculate the total, highest value, and lowest value from a tuple of integers without using the built-in sum(), max(), and min() functions. 5) Write a Python program to filter a tuple . n = (3, 14, 7, 22, 9, 41, 18, 5), keep only values greater than 10 6) Write a Python program to determine how many elements are in a set without using the built-in len() function. s = {"cat", "dog", "bird", "fish"} 7) Write a Python program to combine two sets into one, containing all unique elements from both sets. 8) Write a Python program to find all elements that are common to both sets. s1 = {1, 2, 3, 4} s2 = {3, 4, 5, 6}


t = (1, 2, 3)

result = t * 3

print("Q1:", result)


t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)

result = t1 + t2 + t3

print("Q2:", result)


t = (10, 20, 30, 40)

element = 30

if element in t:
    print("Q3: Element found")
else:
    print("Q3: Element not found")


t = (10, 25, 5, 40, 15)

total = 0
highest = t[0]
lowest = t[0]

for num in t:
    total += num

    if num > highest:
        highest = num

    if num < lowest:
        lowest = num

print("Q4:")
print("Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)


n = (3, 14, 7, 22, 9, 41, 18, 5)

result = ()

for num in n:
    if num > 10:
        result += (num,)

print("Q5:", result)


s = {"cat", "dog", "bird", "fish"}

count = 0

for item in s:
    count += 1

print("Q6: Number of elements =", count)


s1 = {1, 2, 3}
s2 = {3, 4, 5}

result = s1.union(s2)

print("Q7:", result)


s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

result = s1.intersection(s2)

print("Q8:", result)