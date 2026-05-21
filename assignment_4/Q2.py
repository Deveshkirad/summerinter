#Q3 Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def get_dis_element(list):
    distinct_list = []
    for element in list:
        if element not in distinct_list:
            distinct_list.append(element)
    return distinct_list

input_list = input("Enter a list of elements (separated by spaces): ").split()
distinct_elements = get_dis_element(input_list)
print(f"The distinct elements in the list are: {distinct_elements}")
