

my_list = [1, 2, "3", 4, ["A","B","C"]]
my_list.append(5)
my_list.insert(0,10) # Insert 10 at the beginning
my_list.extend([6, 7, 8]) # Extend the list by appending elements from another iterable
my_list.remove(2) # Remove the first occurrence of 2
my_list.pop() # Remove and return the last item
my_list.pop(1) # Remove and return the item at index 1
#my_list.clear() # Remove all items from the list
print(my_list)
# print(my_list[0])
# print(my_list[4])
# print(my_list[4][1])
# print(my_list[-1])
# print(len(my_list))
# print(my_list[:3])
# print(my_list[3:])

# my_list2 = my_list * 2 # This creates a new list by repeating the original list
# print(my_list2)

# my_list3 = my_list + my_list2
# print(my_list3)

print(type(my_list))

