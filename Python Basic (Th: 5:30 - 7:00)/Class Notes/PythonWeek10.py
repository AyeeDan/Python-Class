#Week "10"
#Today we're going to learn about functions
#Example

def greet():
  print("Hello World")

greet()

def your_name(username):
  print(f"Hello, {username}")
  
waterbottle = "Michelle"
your_name(waterbottle)

def add_numbers(num1, num2):
  result = num1 + num2
  return result
  
new_result = add_numbers(1.0,4) + 5
print(new_result)

mult_result = add_numbers(100000000,3)*72
print(mult_result)

global_var = 10

def local_scope():
  local_var = 20
  print("Local Variable:", local_var)
  print("Global Variable:", global_var)

local_scope()

def greet_with_default(name="User"):
  print(f"Hello, {name}!")
  
greet_with_default("gdrfdg")

def split_name(full_name):
  first_name, last_name = full_name.split()
  return first_name, last_name
  
name = input("Please enter your first and last name")
first,last = split_name(name)
print("First Name:",first,"\nLast Name:", last)



















