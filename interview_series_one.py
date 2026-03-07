# Check if a string is a palindrome.
# input_string = input("Enter a string: ")
#str1 = "apple"
# solution1
"""rv_string = input_string[::-1]
if input_string == rv_string:
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")

# solution2
left = 0 
right = len(input_string) - 1
while left < right:
    if input_string[left] != input_string[right]:
        print(f"{input_string} is not a palindrome.")
        break
    left += 1
    right -= 1
else:
    print(f"{input_string} is a palindrome.")

# solution3
input_string= input("Enter the String ")
length=len(input_string)
rev_str=''
for i in range(length-1,-1, -1):
    print('inside loop')
    rev_str = rev_str+input_string[i]

print(rev_str)
if input_string==rev_str:
    print(f"{input_string} is pallindrome")
else:
    print(f"{input_string} is not pallindrome")"""


# Count vowels and consonants in a string.
#input_string = input("Enter a string: ")
"""l_string = input_string.lower()
vowels = 'aeiou'

vowel_count = 0
consonant_count = 0

for char in l_string:
    if char in vowels:
        vowel_count += 1
    
    elif char.isalpha():
        consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")"""
# Reverse the words in a sentence.
"""input_sentence = input("Enter a sentence: ")
words = input_sentence.split()
rev_words = []
for word in words:
    rev_words.append(word[::-1])
reversed_sentence = ' '.join(rev_words)
print(f"Reversed sentence: {reversed_sentence}")


input_sentence = input("Enter a sentence: ")
words = input_sentence.split()
reversed_sentence = ' '.join(reversed(words))
print(f"Reversed sentence: {reversed_sentence}")"""

# 19.	Compress a string using run-length encoding (e.g., aaabb -> a3b2).

"""input_string = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(input_string)):
    if input_string[i] == input_string[i - 1]:
        count += 1
    else:
        result += input_string[i - 1] + str(count)
        count = 1

result += input_string[-1] + str(count)
print(result)"""


"""# Check if a list is sorted.
#input_list1 = [1, 2, 3, 4, 5]
input_list2 = [5, 4, 3, 2, 1]
flag = True
for i in range(len(input_list2) - 1):
    if input_list2[i] > input_list2[i + 1]:
        flag = False
        break
if flag:
    print("List 2 is sorted.")
else:
    print("List 2 is not sorted.")"""

# Find pairs in a list with a given sum.
l1 = [1,2,3,4,5,5,6,7,3,4,1]
target = 10
# algorithm
"""
Pick first element
Compare with all other elements
Check if their sum equals target
"""
for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] + l1[j] == target:
            print(f"Pair found: ({l1[i]}, {l1[j]})")


l1 = [1,2,3,4,5,5,6,7,3,4,1]
print(tuple(l1))
t1 = (3,4,5,6,7,3,4,1)
print(list(t1))
























