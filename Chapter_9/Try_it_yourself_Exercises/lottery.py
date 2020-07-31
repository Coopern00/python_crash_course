# Radovan Novakovity
# Try it yourself 9-14.
#  Make a list or tuple containing a series of 10 numbers and five letters
#  Randomly select four numbers or letters from the list and print a message saying that any ticket matching these four numbers or letters wins a prize

from random import choice

# Creating the list to randomly select from
possibilities = [4, 17, 82, 1, 67, 12, 9, 45, 65, 23, 'e', 'g', 'n', 's', 'b',]

# Creating the emtpy list for the winning numbers
winning_ticket = []
print("Let's see what the winning ticket is...")

# Creating a while loop in order to get the 4 numbers in the list
while len(winning_ticket) < 4:
    # Picks a random number from the list and adds it to the winning_ticket list
    pulled_item = choice(possibilities)

    # Prevents duplications in the list
    if pulled_item not in winning_ticket:
        print(f"We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)

print(f"The final winning ticket is: {winning_ticket}")