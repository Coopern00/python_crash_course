# Radovan Novakovity
# Try it yourself 7-2.
#  Write a program that asks the user how many people are in their dinner group
#  If the answer is more than eight, print a message saying they’ll have to wait for a table
#  Otherwise, report that their table is ready

guest_number = int(input("\nHow many people are in your group? "))
# Converting the input string to an int
#guest_number = int(guest_number)

# Checking the condition
if guest_number > 8:
    print("\nI'm afraid you have to wait a bit to have a proper sized table.")
else:
    print("\nYour table is ready!")