# Q1 Do Practise of Dictionary, Tuple ,Set

#dictionary
d={"Name":"John" , "Age":30 , "City":"New York"}
print(d)
print(d["Name"])
print(d["Age"])

#Nested Dictionary
d={"Name":"John" , "Age":30 , "City":"New York" , "Hobbies":{"Hobby1":"Reading" , "Hobby2":"Traveling"}}
print(d)
print(d["Hobbies"]["Hobby1"])

d[1]="USA"
print(d)

del d[1]
print(d)

d1=d.copy()
print(d1)

d.clear()
print(d)

print(d1.get("Name"))
print(d1.keys())
print(d1.values())
print(d1.items())

print("------")
d2={"Name":"Alice" , "Age":25 , "City":"Los Angeles"}
d1.update(d2)
print(d1)




#tuple
t=(1,2,3,4,5)
print(t)
print(t[0])
print(t[1])

s=(2,4,6,8,10)
print(s)

print(t+s)

t=t*3
print(t)

#set
s1={1,2,3,4,5}
print(s1)

s2={4,5,6,7,8}
print(s2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))





	
	
	