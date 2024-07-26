# 1
full_name = "Lily Hou"

# 2 (many ways to solve this question, more than the number of options provided)
#   option 1
greeting = "Hello, my name is " + full_name
print(greeting) # optional code
#   option 2
greeting = "Hello, my name is "
message = greeting + full_name
print(message)

# 3 (many ways to solve this question)
word_list = full_name.split()
print(word_list[0])

# 4
sentence = input("Please enter a sentence: ")
print("Entered sentence was:", sentence)

# 5
print("The length of the sentence is:", len(sentence))

# 6
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Capitalize the first letter of the sentence:", sentence.capitalize())
print("Count the ocurrences of the letter \"e\" in the sentence:", sentence.count("e"))
print("Check if the question ends with a question mark:", sentence.endswith("?"))

# 7
from datetime import datetime # import datetime module
current_date = datetime.now()
message = f"Today is {current_date}."
print(message)

# 8
day = current_date.day
month = current_date.month
year = current_date.year
message = f"Today is {month}/{day}/{year}."
print(message)

# 9 (many ways to solve this question, more than the number of options provided)
#   option 1
print(f'The result of 5 multiplied by 3 is {5 * 3}.')

#   option 2
a = 5
b = 3
result = a * b
print(f'The result of {a} multiplied by {b} is {result}.')

#   option 3
a = 5
b = 3
result = a * b
print(f'The result of {a} multiplied by {b} is {a * b}.')
