# Radovan Novakovity
# Try it yourself 7-3.
#  Ask the user for a number, and then report whether the number is a multiple of 10 or not

# Asking for a number from the user
number = int(input("\nPlease enter a number to check if It's a multiple of 10 or not: "))
# Converting the string input to an integer
#number = int(number)

# Checking the condition that if modulo returns 0 then yes it is a multiple, if not then it is not a multiple of 10
if number % 10 == 0:
    print(f"\nYes, the number {number} is a multiple of 10.")
else:
    print(f"\nNo, the number {number} is not a multiple of 10.")