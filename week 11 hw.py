#Week 11 HW


#Problem 1
def apply_operation(num1 = "3", num2 = "5"):
    result = num1 + num2
    return result
print(apply_operation)

def apply_operation(num1 = "3", num2 = "5"):
    result = num1 + num2
    return result
print(apply_operation)
def apply_operation(num1 = "3", num2 = "5"):
    result = num1 + num2
    return result
print(apply_operation)
def apply_operation(num1 = "3", num2 = "5"):
    result = num1 + num2
    return result
print(apply_operation)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

is_even = lambda x: x % 2 == 0
even_numbers = list(filter(is_even, numbers))

print(even_numbers) 
def process_numbers(numbers, func):
    return [func(x) for x in numbers]
numbers = [1, 2, 3, 4, 5]
square = lambda x: x ** 2
squared_numbers = process_numbers(numbers, square)

print(squared_numbers)

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
result = power(2, 5)
print(result)

def logger(func):
    def wrapper():
        print(f"Calling function '{func.__name__}' with arguments: {fun} and kwargs: {do}")
       
        return result
    return wrapper
def apply_operation(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        raise ValueError("Unsupported operation")

apply_operation(5, 3, 'add')
apply_operation(10, 2, 'subtract')
apply_operation(4, 7, 'multiply')
apply_operation(8, 2, 'divide')




















































