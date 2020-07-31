# Radovan Novakovity
# Try it yourself 9-15.
#  You can use a loop to see how hard it might be to win the kind of lottery you just modeled
#  Make a list or tuple called my_ticket
#  Write a loop that keeps pulling numbers until your ticket wins
#  Print a message reporting how many times the loop had to run to give you a winning ticket

from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'e', 'g', 'n', 's', 'b',]

# Creating my ticket
my_ticket = [4, 9, 'n', 'b']
# Creating the emtpy list for the winning numbers
winning_ticket = []

# Making a counter to show how many times it had to run in order to win 
number_of_tries = 0
# Setting up a flag for the while loop
won_the_lottery = False

# Creating a while loop which runs until it picks the ones from my_ticket
while not won_the_lottery:
    # Creating a while loop in order to get the 4 numbers in the list
    while len(winning_ticket) < 4:
        # Picks a random number from the list and adds it to the winning_ticket list
        pulled_item = choice(possibilities)

        # Prevents duplications in the list
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    # This is for comparing the elements of winning_ticket and my_ticket lists
    for element in my_ticket:
        if element not in winning_ticket:
            won_the_lottery = False
            number_of_tries += 1
            # If there is an element which does not match then it clears the whole list
            del winning_ticket[:]
        else:
            won_the_lottery = True
        
if won_the_lottery:
    print("We have a winning ticket!")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {number_of_tries} tries to win!")