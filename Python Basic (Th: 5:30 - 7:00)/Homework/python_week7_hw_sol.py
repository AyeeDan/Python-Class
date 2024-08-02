# 1
for i in range (1, 6):
  result = i * i
  print(f"The square {i} is {result}")

# 2
sum = 0
for i in range (1, 6):
  sum += i * i
  print(f"The square {i} is {i * i}")
print("The sum of the squared numbers is: ", sum)

# 3
f_minus_two = 0
f_minus_one = 1
count = 1
while count <= 10:
  if count == 0:
    print(f'Term {count}: 0')
  elif count == 1:
    print(f'Term {count}: 1')
  else:
    f_term = f_minus_two + f_minus_one
    f_minus_two = f_minus_one
    f_minus_one = f_term
    print(f'Term {count}: {f_term}')

  count += 1

# 4
is_negative = True
while is_negative:
  num = int(input("Please enter a number: "))
  if num > 0:
    is_negative = False
    print(f"You have entered the positive number: {num}")

# 5
words = ["watermelon", "food", "python", "c++", "java", "omelette"]
for word in words:
  print(word.upper())

# 6
num = int(input("Please enter a number to find its factorial: "))
count = 1
sum = 1
while count <= num:
  sum *= count
  count += 1
print(f'The factorial of {num} is {sum}')
