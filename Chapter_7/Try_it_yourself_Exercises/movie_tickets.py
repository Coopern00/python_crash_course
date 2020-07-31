# Radovan Novakovity
# Try it yourself 7-5.
#  A movie theater charges different ticket prices depending on a person’s age
#  If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15
#  Write a loop in which you ask users their age, and then tell them the cost of their movie ticket

prompt = "Hello, please state you age: "

while True:
    user_age = input(prompt)
    if user_age == 'quit':
        break
#Converting the string input to actual integer if the input is not 'quit'
    user_age = int(user_age)

#Checking which age group does the user belong to, and charge them accordingly
    if user_age < 3:
        print("\tYou are free to go in!")
    elif user_age < 13:
        print("\tThe cost of your ticket is 10$.")
    else:
        print("\tThe cost of your ticket is 15$.")