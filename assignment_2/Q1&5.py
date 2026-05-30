# Q-1   Write a python program that takes in a student name, class. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class,  and percentage are printed.

Student_name = input("Enter student name: ")
Class = input("Enter class: ")
marks = []
for i in range(5):
    mark = int(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)
total_mark = sum(marks)
percentage = total_mark/5

print("\n--- Student Result ---")

print(f"Name: {Student_name}")
print(f"Class: {Class}")
print(f"Percentage: {percentage:.2f}%")


# Q5) In your last program where you find the total and percentage of a student's marks of 5 subject, find the grade of the student using conditional statement. Eg. grade 'A' if percentage is greator than or equals to 60, 'B' for  percentage is greator than or equals to 50 and less than 60,  'C' for  percentage is greator than or equals to 40 and less than 50,  'D' for  percentage is greator than or equals to 33 and less than 40, otherwise 'Fail'
if percentage >= 60:
    grade = 'A'
elif percentage >= 50:
    grade = 'B'
elif percentage >=  40:
    grade = 'C'
elif percentage >= 33:
    grade = 'D'
else:
    grade = 'Fail'

print(f"Grade: {grade}")