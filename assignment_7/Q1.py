"""#Q1) Practise Pandas Series
	Create a Pandas Series from Dictionary 
	Create a Pandas Series from Lists 
	Access the elements of a Series in Pandas"""

import pandas as pd

pandict = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(pandict)
pandlist = pd.Series([1, 2, 3, 4, 5])
print(pandlist  )     

print(pandict['a'])
print(pandlist[0])

pandict['b'] = 20
print(pandict)
pandlist[1] = 200
print(pandlist)

#min and max
print(pandict.min())
print(pandict.max())
print(pandlist.min())
print(pandlist.max())

#mean
print(pandict.mean())
print(pandlist.mean())