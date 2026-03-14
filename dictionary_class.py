# Dictionary Type
"""
A dictionary is a collection which is unordered, mutable and indexed through keys.
In Python dictionaries are written with curly brackets, and they have keys and values.
"""
"""d1 = {}
print(d1, type(d1), len(d1))
d2 = dict()
print(d2, type(d2), len(d2))
if type(d1) == type(d2):
    print("Both d1 and d2 are of the same type.")

d3 = {"name": "Alice", "age": 30, "city": "New York"}
print(d3, type(d3), len(d3))
d4 = dict(name = "rohan", age = 25, city = "Delhi")
print(d4, type(d4), len(d4))

# Accessing values in a dictionary
print(d3["name"])  # Output: Alice
print(d4["age"])   # Output: 25
print(d4['name'])

print(d3.get("name"))  # Output: Alice)
#print(d3['dob'])

print(d3.get('dob'))  # Output: None
if d3.get('dob') is None:
    print("Key 'dob' does not exist in the dictionary.")"""

"""
Keys must be hashable (immutable types: int, float, str, tuple, frozenset). Lists, dicts, sets are not hashable. Values can be any Python object.
"""
"""data = { 101 : 'a', 
        23.45 : 'b',
        'name': 'deepak',
        #[1,2,3] : 'c'
        (1,2,3) : 'd',
        #{'a':'b'}: 'e',
        'names': ['rohan', 'deepak', 'alice'],
        }
print(data)
print(type(data), data[101], data[23.45], data['name'], data[(1,2,3)])


info = {"name" : "rohan", "age": 25, "city": "Delhi", "dob": "01-01-1998", "mobile": "764764"}
print(info.get("name"))
print(info.get("mobile", "Not Available"))
data = info.get("mobile", "Not Available")
if data == "Not Available":
    print("Mobile number is not available.")
else:
    print(f"Mobile number is: {data}")

# setdefault() method
print(info.setdefault("email", "admin@gmail.com"))
print(info)

data = [("id", 101), ("emp_name", "rohan"), ("emp_age", 25), ("emp_city", "Delhi")]
d1 = dict(data)
print(d1)

data = [["ids", [101, 102]], ["emp_name", "rohan"], ["emp_age", 25], ["emp_city", "Delhi"]]
d2 = dict(data)
print(d2)

keys = ["id", "emp_name", "emp_age", "emp_city"]
d1 = dict.fromkeys(keys, 0)
print(d1)
d1['id'] = 101
d1['emp_name'] = "rohan"
print(d1)
d1['emp_name'] = "deepak"
print(d1)"""

info = {"name" : "rohan", "age": 25, "city": "Delhi", "dob": "01-01-1998", "mobile": "764764"}
print(info.keys())
print(info.values())
print(info.items())

for item in info:
    print(item)
    print(info.get(item))

for key in info.keys():
    print(key)
    print(info.get(key))

for v in info.values():
    print(v)

for k, v in info.items():
    print(k, v)












