print("Double Quotes!")
print('Single Quotes!')

single_quoted = 'Single Quoted Variable'
double_quoted = "Double Quoted Variable"

print(single_quoted)
print(double_quoted)

#Triple quotes require 3 consecutive single quotes
triple_quoted = '''Hello! This is line 1
This is line 2
This is line 3
Triple quotes can span multiple lines!'''

print(triple_quoted)

#Concatenation: Combining strings using the + operator
#Repitition: Repeating strings using the * operator

first_name = "Billy"
last_name = "Jean"

full_name = first_name + " " + last_name
greeting = "Hello, my name is " + full_name

print(greeting)

repeated_text = "Repeat " * 3 #Repeats 3 times
print(repeated_text)


message = "   Type here to search   "
length = len(message)
print(length)

lower_text = message.lower()
print(lower_text)

upper_text = message.upper()
print(upper_text)

stripped_text = message.strip()
print(stripped_text)

word_list = message.split()
print(word_list)

new_text = " Hello!".join(word_list)
print(new_text)

index = message.find("t")
print(index)

replaced_text = message.replace("search", "party!")
print(replaced_text)

total = message.count("e")
print(total)

name = "Beezlebub"
age = 673
formatted_text = f"My name is {name} and I am {age} years old."
print(type(formatted_text))
print(formatted_text)

pi = 3.141592
formatted_number = f"Pi is approximately {pi:.2f}" #pi is rounded to 2 decimals
print(formatted_number)

#Example 1 Reversing a string
text = "I worship glass!!!"
reversed_text = text[::-1]
print("Reversed String:", reversed_text)

#Example 2 Check for a substring (checking valid email)
email = "user@exa.mplecom"
if "@" in email and "." in email:
  print("This is a valid email address.")
else:
  print("This is not a valid email address.")

#Exercise 1: Write a program that counts the number of vowels in a given string"
alphabet = "abcdefghijklmnopqrstuvwxyz" 
a = alphabet.count("a")
e = alphabet.count("e")
i = alphabet.count("i")
o = alphabet.count("o")
u = alphabet.count("u")
vowels = a+e+i+o+u
print(vowels)










