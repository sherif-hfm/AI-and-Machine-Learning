# Sets are unordered collections of unique elements.
set1 = {1,3,'B', 2,'A', 5, 4}
print(type(set1))
print(set1)

set2 = {3, 4, 5, 6, 7}
set2.add(8)
set2.update([9, 10])
#print(set2)
print(set1.union(set2))
#print(set1.intersection(set2))
# print(set1.difference(set2))