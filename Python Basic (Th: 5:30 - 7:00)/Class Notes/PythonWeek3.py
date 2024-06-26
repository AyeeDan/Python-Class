import math

addresult = 5 + 2
print(addresult != 7)

subresult = 5-2
print(subresult >= 3 and addresult == 7)

multresult = 5*2
print(multresult <= 4 or multresult >= 4)

divresult = 5/2
print(divresult)

modulusresult = 5%2
print(modulusresult)

expresult = 5**2
print(expresult)

floordivresult = 5//2
print(floordivresult)

#working on conditions
condition1 = True
condition2 = False

result1 = condition1 and condition2
result2 = condition1 or condition2
result3 = not condition1

print("result1:",result1)
print("result2:",result2)
print("result3:",result3)


#Exercise 1 Find the area of the rectangle with length = 48 and width = 6345
print(math.sqrt(81))

#Introduction to if statements
age_friend = int(input("What is the age of your friend?"))
age_me = int(input("What is your age?"))
if age_me > age_friend:
  print("I'm older than my friend!")
elif age_me < age_friend:
  print("I'm younger than my friend!")
else:
  print("We must be the same age!")


#Exercise 2: Write a program that checks if a given number is even
#(use the modulus operator).

#Exercise 4: Create a logical expression that checks if you have both 
#ice cream and chocolate, and print whether you can make a delicious dessert.


