#Hw 10

#Problem 1
def greet_user(username):
    print(f"Hello,{username}!")

greet_user("Jackie")

def square_number(number):
    result = number**2
    print(result)
    return result

#Problem 2
def calculate_area(length, width):
    length = 4
    width = 6
    area_total = length*width
    print(area_total)

calculate_area(5,3)
print(calculate_area)


#Problem 3

def divide_numbers(num1, num2):
    quotient = num1//num2
    remainder = num1 % num2
    return quotient, remainder
num1 = 9
num2 = 3

quotient, remainder = divide_numbers(quotient, remainder)

print(f"Quotient: {quotient}, Remainder: {remainder}")

def calculate_sum(*args):
    return sum(args)


result = calculate_sum(5, 10, 15)
print(f"Sum: {result}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(f"Factorial of 5: {result}")

result = factorial(7)
print(f"Factorial of 7: {result}")




























