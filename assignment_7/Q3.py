"""Q3)Data iteration
	Different ways to iterate over rows in Pandas Dataframe 
	Selecting rows in pandas DataFrame based on conditions 
	Select any row from a Dataframe using iloc[]
	Limited rows selection with given column
	Drop rows from the dataframe based on certain condition applied on a column 
	Insert row at given position in Pandas Dataframe 
	Create a list from rows in Pandas dataframe """

import pandas as pd
data={
    "Name":["Aman","Rahul","Priya"],
    "Age":[20,21,19],
}
df=pd.DataFrame(data)
print(df)

#iterating over rows
print("\niterating over rows\n")

for index,row in df.iterrows():
    print(index,row["Name"],row["Age"])

print(df.iloc[1]["Name"]) 

#selecting on condition

print(df[df["Age"]>19])

print(df[(df["Age"]>19) & (df["Name"]=="Aman")])

#Using iloc
print("\nusing iloc\n")

print(df.iloc[[0,2],[0,1]])

print(df.iloc[1:3,0:2])

#DROP

print("\ndroping rows\n")

print(df.drop(df[df["Age"]<=19].index))

print(df)

#inserting row

print("\nInster a row at index 1\n")
newrow={"Name":["Sita"],"Age":[18]}
new_row=pd.DataFrame(newrow)

df1=df.iloc[:1]
df2=df.iloc[1:]

df=pd.concat([df1,new_row,df2]).reset_index(drop=True)
print(df)

