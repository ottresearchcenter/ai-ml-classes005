"""l1 = [100, 200]
l2 = l1
print(l1)
print(l2)
print(id(l1), id(l2))
l2[0] = 500
print(l1)
print(l2)
import copy

#shallow copy
l3 = copy.copy(l1)
print(l3)
print(id(l1), id(l3))
l3[0] = 1000
print(l1)
print(l3)

data = [100, ['a', 'b', 'c'], 300, 400, 500]
data1 = copy.copy(data)
print(data)
print(data1)
print(id(data), id(data1))
data1[1][1] = 'bb'
print(data)
print(data1)

# deep copy
data2 = copy.deepcopy(data)
print(data2)
data2[1][1] = 'ddd'
print(data)
print(data2)"""

"""# list pre defined functions
data = []
data.append("apple")
print(data)
data.append("banana")
print(data)
my_list = []
for i in range(1, 21):
    my_list.append(i**2)
print(my_list)
my_list.insert(2, 9000)
print(my_list)
l1 = [1,2,3,4,5]
# [1,2,3,3,4,5]
# [1,2,9000,3,4,5]
index = 2
data = 9000
result = l1[:index] + [data] + l1[index:]
print(result)"""

"""# append and extend
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = []
l4 = []
l3.append(l1) # adding the entire list as a single element to l3
l3.append(l2) # adding the entire list as a single element to l3
print(l3)
print(len(l3))
l4.extend(l1)
l4.extend(l2)
print(l4)
print(len(l4))"""
# remove, pop and clear
fruits = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
fruits.remove('date')  # Removes 'date' from the list
fruits.remove(fruits[1])
print(fruits)
fruits.pop()  # Removes the end element ('grape') from the list
print(fruits)
fruits.pop(1)  # Removes and returns the element at index 1 ('banana')
print(fruits)
fruits.clear()  # Removes all elements from the list
print(fruits)
del fruits  # Deletes the entire list
#print(fruits)

# Home Work 
# -> index, count and sort
# Flatten a nested list (arbitrary depth)
# Find common elements between two lists (with and without sets)











