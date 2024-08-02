"""
Python-week8-notes.py
Dicitonaries and sets

Built in data types in python: integer, float, strings, list, dictionaries, and sets.
There are other built in data structures that works similar to list: dictionaries, sets, and tuples.


Dictionaries and sets are data structures that will help us organize our data. It also allows us to manipulate them efficiently and store them.

Dictionaries: store data as key-value pairs, this provides a quick access to values based on their unique keys

Set: store UNIQUE element, and are also used for tasks like duplication and membership testing. Sets stores the data in an unordered way.
"""

# Dictionary example:
student = {
    "name": "Lily",
    "age": 100,
    "grade": "senior"
}
print(student)

# Set example:
colors = {"red", "green", "blue"}
print(colors)

#list = [] # empty list
#student = {} # empty dictionary | student.dict()
#colors = set() # empty set

# How do we get the value from the key "name" from our dictionary `student`?
name = student["name"]
print(f'The name is {name}')

# Challenge: try getting the values of age and grade from the student dictionary
age = student["age"]
grade = student["grade"]
print(f'{age} | {grade}')

# how do we modify the value of a specific key?
student["age"] = 200
print(student["age"])

# Challenge: change the value of name and grade from the student dictionary
#   print the entire dictionary

for var in student:
  print(var) # it only prints the key

for var in student:
  print(student[var]) # it only prints the value

student.pop("age") # remove a key-value pair from a dictionary
print(student)

# Set is known to be as a more efficient data structure than list, tuples, dictionaries, and hash maps
# the reason is because set uses less time to store the data
# set also ensures that they are no duplicated

# Set has some built in methods: intersection, union, and difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set_1 = set1.difference(set2)
difference_set_2 = set2.difference(set1)
print(union_set)
print(intersection_set)
print(difference_set_1)
print(difference_set_2)

text = "python programming"
char_count = {}

for char in text:
  if char.isalpha():
    char = char.lower()
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1

print("Character count: ", char_count)

# Example of set
fruits = ["strawberry", "guava", "mango", "guava"]
unique_fruits = set(fruits)
print(fruits)
print("Unique fruits: ", unique_fruits)

"""- Dictionary: A data structure that stores data as key-value pairs, allowing quick access to values using unique keys.
- Set: A data structure that stores unique elements and supports set operations like union and intersection.
- Key: A unique identifier used to access values in a dictionary.
- Value: Data associated with a key in a dictionary.
- Union: A set operation that combines two sets and returns the elements present in either or both sets.
- Intersection: A set operation that returns the common elements between two sets.
- Difference: A set operation that returns the elements present in one set but not in the other.
"""

# Exercise 1: Create a dictionary to store information about a book (title, author, year of publication) and print the book's details.
# Exercise 2: Add a new item to the book dictionary (book location or genre)
# Exercise 3: Given a list of numbers, create a set of unique numbers from the list.
# Exercise 4: Write a program that counts and prints the frequency of each word in a given text.

# Excercise 1:
book = {
    "title": "Perks of Being a Wallflower",
    "author": "Stephen Chbosky",
    "year": 2012
}
print(book)

# Exercise 2:
book["location"] = "USA"
print(book)

# Exercise 3:
list = [3, 7, 5, 9, 2, 5, 3]
unique_numbers = set(list)
print(unique_numbers)

# Exercise 4:
text = "python programming"
char_count = {}
for char in text:
  if char.isalpha():
    char = char.lower()
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1

print("Character count: ", char_count)
