"""Q 2) DataFrames
	Make a Pandas DataFrame with a two-dimensional Python list 
	Create DataFrame from Python dict 
	Create Pandas dataframe using list of lists 
	Create a Pandas dataframe using list of tuples 
	Create a Pandas DataFrame from List of Dicts """

import pandas as pd

print("\nusing dictionary \n")
data = {
    "Name": ["Aman", "Rahul", "Priya"],
    "Age": [20, 21, 19],
    "City": ["Jaipur", "Delhi", "Mumbai"]
}
df = pd.DataFrame(data)
print(df)

print("\nDF using list of list \n")
data2 = [
    ["Aman", 20, "Jaipur"],
    ["Rahul", 21, "Delhi"],
    ["Priya", 19, "Mumbai"]
]
df2 = pd.DataFrame(data2,columns=["Name","Age","City"])
print(df2)

print("\nDF using list of tuples \n")
data3 = [
    ("Aman", 20, "Jaipur"),
    ("Rahul", 21, "Delhi"),
    ("Priya", 19, "Mumbai")
]
df3 = pd.DataFrame(data3,columns=["Name","Age","City"])
print(df3)

print("\nDF using list of dicts \n")
data4 = [
    {"Name": "Aman", "Age": 20, "City": "Jaipur"},
    {"Name": "Rahul", "Age": 21, "City": "Delhi"},
    {"Name": "Priya", "Age": 19, "City": "Mumbai"}
]


