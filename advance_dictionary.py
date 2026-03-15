"""emp_info = {
    "id": 101,
    "emp_name": "rohan",
    "dob": "01-01-1998",
    "mobile": "764764",
    "address": {
        "flat No": 101,
        "street": "Main Street",
        "city": "Delhi",
        "state": "Delhi",
        "country": "India",
        "tmp_address": {
            "flat No": 202,
            "street": "Second Street",
            "city": "Mumbai",
        }
    }
}
print(emp_info["address"]["city"])
print(emp_info["address"]["tmp_address"]["street"])"""

# zip function

"""
The zip() function is used to combine multiple iterables (lists, tuples, etc.) element-wise. It pairs the first elements together, the second elements together, and so on.
"""
from poetry import json


students = ["rohan", "deepak", "sachin", "suresh"]
marks = [85, 90, 78, 92]

data  = zip(students, marks)
print(list(data))

students = ["rohan", "deepak", "sachin", "suresh", "vijay"]
marks = [85, 90, 78, 92]
data  = zip(students, marks)
print(list(data))

# most common use case for ai/ml applications is to create a dictionary from two lists using zip() function.
headers = ["name", "age", "salary"]
values = ["rohan", 25, 50000]
data = zip(headers, values)
#print(list(data))
info = dict(data)
print(info)

headers = ["name", "age", "salary"]
values = [["rohan", "deepak", "sachin"], [25, 30, 28], [50000, 60000, 55000]]
print(dict(zip(headers, values)))

# unzipping 
"""
what is unzipping?
Unzipping is the process of reversing the zip operation. It takes a zipped object and separates it back into its original components. This is typically done using the zip() function with the unpacking operator (*).
"""
data = [("rohan", 85), ("deepak", 90), ("sachin", 78), ("suresh", 92)]
names, marks = zip(*data)
print(names, marks)
print(list(names))
print(list(marks))

# parallel iteration using zip() function
list1 = [1,2,3,4,5]
list2 = [10, 20, 30, 40, 50]
for i, j in zip(list1, list2):
    print(i, j)

# Problem Statement: check if both list are identical but we want to iterate over them in parallel and print the sum of corresponding elements.
list1 = [1,2,3,4,5]
list2 = [1,2,6,4,5]
if len(list1) != len(list2):
    print("Both lists are not identical.")
else:
    for i, j in zip(list1, list2):
        if i != j:
            print("Both lists are not identical.")
            break
        print(i + j)

# Problem Statement: We have list of names and list of posts. Names can be duplicate due to dynamic nature of application but we want to create a dictionary of name and post. If there are duplicate names, we want to store the posts in a list.
fb_profiles = ["rohan", "deepak", "sachin", "rohan", "suresh", "deepak", "vijay", "vijay", "vijay"]
fb_posts = ["post1", "post2", "post3", "post4", "post5", "post6", "post7", "post8", "post9"]
profile_posts = {}
for profile, post in zip(fb_profiles, fb_posts):
    if profile in profile_posts:
        profile_posts[profile].append(post)
    else:
        profile_posts[profile] = [post]
print(profile_posts)

# implementing in-memory cache for ai/ml applications with simple dictionary
cache = {}
def expensive_computation(x):
    if x in cache:
        print("Fetching from cache...")
        return cache[x]
    else:
        print("Performing expensive computation...")
        result = x * x  # Simulating an expensive computation
        cache[x] = result
        return result
print(expensive_computation(10))  # Performing expensive computation...
print(expensive_computation(10))  # Fetching from cache...

# JSON Serialization and Deserialization
import json

data = {
    "name": "rohan",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "traveling", "cooking"]
}

with open("test1.json", "w") as f:
    json.dump(data, f)

with open("test1.json", "r") as f:
    data = json.load(f)
    print(data)
    print(type(data))

# My Suggestions for dictionary data structure in ai/ml applications:
"""
Lookup vs list: Dict lookup O(1) vs list search O(n). For large datasets, dicts are essential.
Memory overhead: Dicts use more memory than lists because of hash table overhead. For huge data, consider alternatives like array or numpy arrays if you can use integer indices.
Key choice: Integers and strings are fastest. Avoid custom objects as keys unless necessary.
"""