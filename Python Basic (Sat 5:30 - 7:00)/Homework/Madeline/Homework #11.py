def apply_operation(num1, num2):
  result = num1 * num2
  return result

print (apply_operation(3,4))
       
hello = apply_operation(1,2)+5
print(hello)

hey = apply_operation(3,5)/2
print(hey)

hi = apply_operation(7,9)-8
print(hi)

print ("")
list_1 = [5,6,7,8,898,4,3,2,3,4,2,3,31,2,2,3,4,5,6,7,8,9,4,1]
lamb_da = list(filter(lambda x: x % 2 == 0, list_1))
print (lamb_da)
print ("")

def process_numbers(numbers, func):
    return [func(number) for number in numbers]

myresult = process_numbers(list_1, lambda x: x * 2)
print(myresult)
print ("")
def power(base, exponent):
  if exponent == 0:
    return 1
  else:
    return base * power(base, exponent - 1)

yourresult = power(2, 5)
print(yourresult)

print ("")
print ("I got help with this last one, it's complicated.")
       
import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
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
        return None

print(apply_operation(5, 3, 'add'))
print(apply_operation(10, 2, 'subtract'))
print(apply_operation(6, 7, 'multiply'))
print(apply_operation(8, 4, 'divide'))










