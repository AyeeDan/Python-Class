print("Begin Fruits loop")
fruits = ["apple", "banana", "mango"]
for i in fruits:
  print(i)
  
print("Begin Pizza Loop")  
for pizza in range(0,10):
  print(pizza)

print("Begin count loop")  
count = 1
while count <= 6:
  print("Count:", count)
  count += 1
  
print(count)

print("Begin count 2 loop")  
count = -4
while count <= 0:
  print("Count:", count)
  count += 1
  
print(count)

#Example 1
#Continue vs. Break
print("Find even numbers")
numbers = [1,2,3,4,5,6,7,8,9,10]

for f in numbers:
  if f%2 == 0:
    print("Even:",f)
    break
  else:
    print("Im gunna take a break!")
print("I'm FREE")

#Example 2
print("Sum of Numbers")
total = 0
for num in range(1,6):
  total += num
print("Here is your total, sir or ma'am:", total)

#Example 3
print("Finding Prime Numbers")
prime_numbers = []

for num in range(2,20):
  is_prime = True
  for i in range(2,num):
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
    prime_numbers.append(num)

print("Prime Numbers:",prime_numbers)
















