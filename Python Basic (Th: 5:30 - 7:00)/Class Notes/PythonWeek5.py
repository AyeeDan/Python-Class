#Week 5: Lists and Tuples

#When creating a list we use square brackets
#Lists are mutable
#Mutable means that it can be edited
vegetables_list = ['Cabbage', "Broccoli", "Beat", "Carrot"]

veggie = vegetables_list[2]

print(veggie)
print("Adding a tomato to the list using the append function")
vegetables_list.append("Tomato")
print(vegetables_list)

vegetables_list.insert(2,"Pea")
print(vegetables_list)

#vegetables_list.remove("Cabbage")
#print(vegetables_list)

vegetables_list[2] = 7
print(vegetables_list)

print(vegetables_list[3])

#Taste of for loops if you want to get ahead
for i in range(len(vegetables_list)):
    print(vegetables_list[i])

numbers_tuple = (53, 23,7)

#Unpacking a tuple
number1, number2 = numbers_tuple[0],numbers_tuple[1]
number3, number4,number5 = numbers_tuple
print(number1,number2)
print(number3,number4,number5)
#This will give you an error -> numbers_tuple.append("7")

sliced_list = vegetables_list[0:len(vegetables_list)//2]
print(sliced_list)

print(len(vegetables_list))

response = " "

while response != "No":
    response = input("Enter a value that you would like to add to your list")
    if response != "No":
        vegetables_list.append(response)

print(vegetables_list)







