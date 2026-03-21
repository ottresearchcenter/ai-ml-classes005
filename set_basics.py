# Set
""" A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (cannot be changed). However, a set itself is mutable. We can add or remove items from it. Sets are defined by enclosing elements in curly braces {}. 
"""

"""s1 = set()
print(s1)
print(type(s1))
print(len(s1))
fruits = {"apple", "banana", "cherry", "apple", "banana", "cherry"}
print(fruits)
print(type(fruits))
print(len(fruits))
l1 = [1, 2, 3, 4, 5, 1, 2, 3, 10, 20, 30,40, 50,60, 70, 80, 90, 100]
s2 = set(l1)
print(s2)
print(type(s2))
print(len(s2))
l1 = sorted(list(s2))
print(l1)

str1 = "hello world, india is my Country. India is a Great country."
print(len(str1))
s3 = set(str1)
print(s3)
print(len(s3))
print(sorted(s3))"""

"""s1 = {'a', 'b', 'c'}
s1.add('d')
print(s1)
s2 = {'e', 'f', 'g'}
s1.update(s2)
print(s1)
s1.add('a')
print(s1)
print(s1.remove('b'))
print(s1)
s1.remove('b')
print(s1.discard('b'))
print(s1)
s1.pop()
print(s1)"""
"""
pop() is useful when you need to process elements one by one without caring about order. However, because sets are unordered, you cannot rely on which element you get. If you need to remove a specific element, it's better to use remove() or discard() instead of pop().
"""
"""print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)
s1.add('x')
s1.add('y')
s1.add('z')
print(s1)
del s1
print(s1)"""

"""
# membership testing
s1 = {'x', 'y', 'z'}
print('x' in s1)
print('a' in s1)

# set math operations
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
data = s1.union(s2)
print(data)
data1 = s1 | s2
print(data1)

data = s1.intersection(s2)
print(data)
data1 = s1 & s2
print(data1)


data = s1.difference(s2)
print(data)
data1 = s1 - s2
print(data1)

data = s2.difference(s1)
print(data)
data1 = s2 - s1
print(data1)"""

"""s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {3,6,7,10}
print(s2.issubset(s1))
print(s2 <= s1)
print(s1.issuperset(s2))
print(s1 >= s2)"""

# frozenset
"""
A frozenset is an immutable version of a set. Once created, you cannot add or remove elements. Because it is immutable, it is hashable and can be used as a key in a dictionary or as an element of another set.
"""
"""fs1 = frozenset([1, 2, 3, 4, 5])
print(type(fs1))
#fs1.add(6)  # This will raise an AttributeError because frozensets do not support adding elements.
info = {"name": "rohan", "age": 25, "hobbies": frozenset(["coding", "gaming", "traveling"])}
print(info)
# frozenset as key of a dictionary
fs2 = frozenset(["python", "java", "c++"]) 
data = {fs2: "programming languages"}
print(data)

s1 = {1, 2, 3}
s2 = {4,5,6}
data = {frozenset(s1), frozenset(s2)}
print(data)
#data = {100, "hello", tuple([1,2,3]), (6,7,6), {"a":"b"}, {1,2,3}, frozenset([4,5,6])}
#print(data)
data = {100, "hello", tuple([1,2,3]), (6,7,6), frozenset({1,2,3}), frozenset([4,5,6])}
print(data)"""


train_labels = {"cat", "dog", "bird", "fish"}
test_labels = {"cat", "dog", "hamster", "rabbit"}
total_labels = train_labels | test_labels
print(total_labels)
common_labels = train_labels & test_labels
print(common_labels)




























