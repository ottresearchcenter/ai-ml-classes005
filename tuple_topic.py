# defination and other details of tuple topic
"""
tuple is a collection which is ordered and unchangeable. it Allows duplicate members.
Tuples are defined using parentheses () and elements within tuple separated by comma. Once a tuple is created, you cannot modify its contents, which makes it immutable. This immutability can be advantageous in situations where you want to ensure that data remains unchanged throughout the execution of a program.
"""
"""t1 = (1,2,3,4,5,3,3,8,90, 'apple', 'banana', 'cherry', [1, 2, 3], (4, 5, 6), True)
print(t1)
print(type(t1))
print(len(t1))
print(t1[0])  # Accessing the first element
print(t1[1])  # Accessing the second element
print(t1[2])  # Accessing the third element
print(t1[3])  # Accessing the fourth element
rev_t1= t1[::-1]
print(rev_t1)
#t1[2] = 1000 # This will raise a TypeError because tuples are immutable
# count, index, slicing, concatenation, repetition, membership testing
print(t1.count(3))  # Count occurrences of 3 in the tuple
print(t1.index(90))  # Get the index of the first occurrence of 3 in the tuple
print(t1.index('apple'))
for value in t1:
    print(value)

# unpacking of tuple
data = ("apple", "banana", "cherry")
fruit1, fruit2, fruit3 = data
print(fruit1)
print(fruit2)
print(fruit3)
first_fruit, *other_fruits = data
print(first_fruit)
print(other_fruits)

if 'banana1' in data:
    print("Found 'banana' in the tuple.")
elif 'grape' in data:
    print("Found 'grape' in the tuple.")
else:
    print("Neither 'banana' nor 'grape' found in the tuple.")


x, y , *z = 100, 200, 300, 400, 500, 600
print(x)
print(y)
print(z)"""

# paired tuple with for loop
pair = [101, 'Alice', 'delhi'], [102, 'Bob', 'mumbai'], [103, 'Charlie', 'bangalore']
for id, name, city in pair:
    print(id, name, city)
    #print(f"ID: {id}, Name: {name}, City: {city}")