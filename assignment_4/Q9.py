#Q9. Write a Python function that accepts a string and counts the number of upper and lower case letters. 
def count_case(input_str):
    uc=0
    lc=0
    for c in input_str:
        if c.isupper():
            uc+=1
        elif c.lower():
            lc+=1
    
    return uc,lc

input_string = input("Enter a string: ")
upper_count, lower_count = count_case(input_string)
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")
