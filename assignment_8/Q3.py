"""3) Create three DataFrames. Vertically concatenate two of them using pd.concat(), then merge the resulting DataFrame with the third DataFrame on a common key. """
import pandas as pd

df1 = pd.DataFrame({
    'Id': [1, 2, 3], 
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'Id': [4, 5, 6],
    'Name': ['David', 'Eve', 'Frank']
})
df3 = pd.DataFrame({
    'Id': [1, 2, 3, 4, 5, 6],
    'Age': [25, 30, 35, 40, 45, 50]
})

df1_new= pd.concat([df1, df2], ignore_index=True)
print("Concatenated DataFrame:")    
print(df1_new)

df_merged = pd.merge(df1_new, df3, on='Id', how='inner')
print("\nMerged DataFrame:")
print(df_merged)