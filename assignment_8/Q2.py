"""2)Create two DataFrames, df1 and df2, with a common column (e.g., 'ID'). 

>Perform an inner merge on this common column and display the resulting DataFrame.
>Perform a left join of df1 and df2 on the 'ID' column. Explain how missing values are handled in the resulting DataFrame. Right Join and Index-Based Join.
>Perform a right join using pd.merge() on a common column, then perform a join using df.join() based on the index. Compare the results. Merging with Multiple Keys."""

import pandas as pd

df1 = pd.DataFrame({
    'Id': [1, 2, 3, 4],
    'Name': ['Devesh', 'Rohit', 'Satyarth', 'Shivam']
})

df2 = pd.DataFrame({
    'Id': [3, 4, 5, 6], 
    'Age': [25, 30, 35, 40]
})

df_inner = pd.merge(df1, df2, on='Id', how='inner')
print("Inner Merge Result:")
print(df_inner)

df_left = pd.merge(df1, df2, on='Id', how='left')
print("\nLeft Join Result:")
print(df_left)

"""In the left join, all records from df1 are included in the resulting DataFrame. If there is a matching 'Id' in df2, the corresponding 'Age' value is included. If there is no match, the 'Age' value will be NaN (Not a Number), indicating a missing value."""

df_right = pd.merge(df1, df2, on='Id', how='right')
print("\nRight Join Result:")
print(df_right)


#join
df_joined=df1.set_index('Id').join(df2.set_index('Id'), how='right')
print("\nJoin using df.join() based on index:")
print(df_joined)