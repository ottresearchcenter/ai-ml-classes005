"""str1 = "this is ai model."
for value in str1:
    print(value)
print(len(str1))
# remove duplicate character
str2 = "this is ai model."
result = ""
for value in str2:
    if value not in result:
        result += value
print(result)
sentence = "AI is transforming the world"
#solution 1
sen="this is  tranformation  in     \n ai . hi, & welcome to ai world."
count=0
for i in sen:
    if i ==" ":
        count+=1
print(count+1)
#solution 2
print(sen.split())
print(len(sen.split()))"""

# List Data 
"""
Lists are mutable, dynamic arrays that serve as the backbone for handling datasets, feature vectors, and model outputs in AI/ML applications.

It can contain elements of different data types, including numbers, strings, and even other lists. Lists are defined using square brackets [] and elements within list sparated by comma. It can be modified after creation, allowing for dynamic data manipulation.
"""
"""my_list = [100, 3.14, "AI", [1, 2, 3], True]
print(id(my_list))
my_list[2] = "AI/ML"
print(my_list)
print(id(my_list))
data = [100, 200, 300, 400, 500]
print(data[0])  # Accessing the first element
print(data[1])  # Accessing the third element
print(data[2])  # Accessing the last element
n = len(data)
print(n)
print(data[-n])
print(data[-1])
print(data[n-1])"""


data = ['AI', 'ML', 'DL', 'NLP', 'CV', 'RL']
sub_list = data[1:4] # Extracting a sublist from index 1 to 3
print(sub_list)
sub_list2 = data[2:] # Extracting a sublist from index 2 to the end
print(sub_list2)
sub_list2 = data[2:200] # Extracting a sublist from index 2 to the end
print(sub_list2)
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

# Extracting a sublist from index 3 to 8 with a step of 2

sub_list3 = my_list[3:130:2]
print(sub_list3)
rev_list = my_list[::-1]
print(rev_list)
rev_list = my_list[::-2]
print(rev_list)
for i in my_list:
    print(i)
print("Sum of all values in the list:")
sum = 0
for i in my_list:
    sum += i
    print(sum)
print(sum)

print("Range of numbers")
for i in range(5, 20, 1):
    print(i)
data = [100, 200, 300, 400, 500]
data.append(600)
print(data)
print("solu1")
for i in range(0, 5):
    print(i)
    print(data[i])
print("solu2")
for i in range(5):
    print(i)
    print(data[i])
data.append(700)
n = len(data)
print("solu3")
for i in range(n):
    print(i)
    print(data[i])











