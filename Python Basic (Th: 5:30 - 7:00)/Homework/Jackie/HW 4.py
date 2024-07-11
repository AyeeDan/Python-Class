#HW 4
#PROBLEM 1

num1_input = int(input("Please enter an integer : "))
#allows you to ask the viewer to input something

if num1_input<0:
    print("Your integer is a negative number!") 

elif num1_input>0:
    print("Your integer is a positive number!")

else:
    print("Your integer is 0!")

#PROBLEM 2

age = int(input("Please enter your age: "))

if age<=12:
    print("You are a child")

else:
    if age<=19:
        print("You are a teenager")

else:
    if age <=59:
        print("You are an adult")

else:
    print("You are a senior")



if age >=18:
    print("Since you are over 18, you have a right to vote!")
          
