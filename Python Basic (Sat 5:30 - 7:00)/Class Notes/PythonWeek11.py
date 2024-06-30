# tkinter
# UI  (user interface)
# GUI (graphic user interface)

# what are functions? 
# functions store information
# functions are a blcok of code that can do a specific for me

# create a function called `greet_user` that takes one paremeter called `name`
# greet_user functions should return the following message: `Hello, name`
def greet_user(name):
  return f"Hello, {name}"
  
someVariable = "Passenger Princess"
print(greet_user(someVariable))

# create a function called `happy_birthday` that wishes someone happy birthday, 
# one paremeter as the name
def happy_birthday(name):
  print(f"happy birthday, {name}!")
  
happy_birthday("froggie")

# functions with default paremeters 
def greet_with_default(name="user"):
  print(f"hello, {name}")
  
greet_with_default()

# function with variable lenght paremeters 

def sum_number(*numbers):
  total = 0
  for num in numbers:
    total += num
  print(total)

sum_number(2, 3, 4)

# create a function that takes variable-length argument lists
# return the product of the variable
# called the function `product_number`
def product_number(*number):
  total = 1
  for num in number:
    total *= num
  print(total)
  
product_number(23, 100, 25)

# lambda function
# a lambda function in python is used for creating small and aanonymous functions
add = lambda x, y: x + y
print("add lambda function result:", add(3,5))

# create a lambda function that multiplies 3 variables and print the result
product = lambda x, y, z: x * y * z
print("product result: ", product(1,2,3))

# recursive functions: are functions that call themselve until certain 
# criteria is met

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
  
print("factorial result: ", factorial(4))

# the first time that we call factorial(4) it's going to return 
# 4 * facotorial(4 - 1) -> 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * factorial(1)
# 4 * 3 * 2 * 1 * factorial(0)
# 4 * 3 * 2 * 1 * 1 