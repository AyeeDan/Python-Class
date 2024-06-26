age = int(input("How old are you"))

print(type(age))

if age >=20:
  print("You are older than 20")
elif age <20:
  print("You are younger than 20")
else:
  print("Error")
  
num = 4

if num%2 == 0:
  print("This number must be even!")
else:
  print("This number is definitely odd!")
  
if 9%2:
  print("Odd")
if 8%2:
  print("Even")
  
  
temperature = 450

if temperature > 100:
  print("Whoa its hot outside")
elif temperature > 50:
  print("Its a nice day outside!")
else:
  print("Its a bit chilly huh")

score = int(input("What is your grade"))

if score == 100:
  print("A+")
elif score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70:
  print("C")
elif score >= 60:
  print("D")
elif score >= 50:
  print("F!!")
  
x = 10
y = 10
if x>y:
  if x%2 == 0:
    print("X is greater than Y AND x is also even")
  else:
    print("X is greater than Y and x is NOT even")
else:
  print("Y is greater than X")


#basic calculator
num1 = float(input("Enter your first number"))
operator = input("Enter an operator (+,-,*,/)")
num2 = float(input("Enter your second number"))

if operator == "+":
  print(num1+num2)
elif operator == "-":
  print(num1-num2)
elif operator == "*":
  print(num1*num2)
elif operator == "/":
  if num2 == 0:
    print("Error: Dividing by 0")
  else:
    print(num1/num2)
    
    
  






















