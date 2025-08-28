# Dictionaries are collections of key-value pairs.
dict1 = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(type(dict1))
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#dict1.clear()
#exit()
dict1['age'] = 26
dict1['country'] = 'USA'
print(dict1)

dict2=dict1.copy()
print(dict2)