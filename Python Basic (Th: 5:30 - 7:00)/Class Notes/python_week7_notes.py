"""
Python-week7-notes.py

Python Lesson 7: Loops (for and while) in Python

- Loops are used to control structures that will allow you to repeat a block of code multiple times.
- Loops are essential for autmating repetitive taks and iterating over collections of data.

- For loops: they are mainly used to iterave over a sequence
  - list, tuples, strings, and range
"""

# Example:
fruits = ["watermelon", "guava", "strawberry"]

for fruit in fruits:
  print(fruit)

# Example (create a list of your top 3 favorite colors and print each color from the list)
colors = ["red", "green", "blue"]
for color in colors:
  print(color)

"""While loops: is used to repeat something until a specific condition is met."""

# Exmaple:
jumping_jack = 1

while jumping_jack <= 10:
  print("Jump number: ", jumping_jack)
  jumping_jack += 1

# Example 2 (create a while loop that prints the numbers from 5 to 20):
num = 5
while num <= 20:
  print("Number: ", num)
  num += 1

# Example 3 (create a while loop the prints the numbers from 5 to 20 that are divisible by 5)
num = 5
while num <= 20:
  print("Number: ", num)
  num += 5

"""
- "break": Terminates the loop prematurely
- "continue": skips the current iteration and continues to the next one.
"""

# Example of using the `continue` keyword in a for looop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
  if number % 2 == 0:
    print("Even number: ", number)
  else:
    continue

# Example of using the `break` keyword in a for loop
for number in numbers:
  if number == 5:
    break
  print("Number: ", number)

"""
For loops with range function
The "range()" function generates a sequence of numbers, which can be used with "for" loops to specify a range of iterations.
"""

# Example:
for i in range(1, 10):
  #print(i)
  continue

# Example (create a for loop that prints the number from 3 to 12, and the total as well)
total = 0
for i in range(3, 12):
  print(i)
  total += i
print("Total: ", total)

# Challenge: use a for loop to find the prime numbers from 2 to 20. store the
#   prime numbers in a list called `prime_numbers`
prime_numbers = []
for num in range(2, 20):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print("Prime numbers:", prime_numbers)

# Exercise 1: Create a program that calculates and prints the factorial of a given number.
# example using `while` loop
ans = 1
start = 1
num = int(input("Please enter a number: "))
while start <= num:
  ans *= start
  start += 1
print("Result: ", ans)

# example using a `for` loop
res = 1
num = int(input("Please enter a number: "))
for i in range(1, num + 1):
  res *= i
print("Result: ", res)


# Conclusion: 
# In this lesson, you've learned about "for" and "while" loops in Python, which are used for repetitive tasks and iterations. Loops are powerful tools for automating tasks and processing data efficiently.
# Continue practicing with loops to become proficient in using them for various programming challenges.

# Vocabulary Words and Definitions:
# - Loop: A control structure that allows you to repeat a block of code multiple times.
# - Iteration: Each execution of the loop's code block is called an iteration.
# - Sequence: An ordered collection of elements, such as a list, tuple, string, or range.
# - Loop Control Statements: Statements like "break" and "continue" that control the flow of loops.
# - Range: A function that generates a sequence of numbers for use in loops.
