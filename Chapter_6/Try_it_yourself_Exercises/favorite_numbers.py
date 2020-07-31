# Radovan Novakovity
# Try it yourself 6-2.
#  Use a dictionary to store people’s favorite numbers
#  Think of five names, and use them as keys in your dictionary
#  Think of a favorite number for each person, and store each as a value in your dictionary
#  Print each person’s name and their favorite number
#  For even more fun, poll a few friends and get some actual data for your program

# Try it yourself 6-10.
#  Modify your program from Exercise 6-2 so each person can have more than one favorite number
#  Then print each person’s name along with their favorite numbers

favorite_numbers = {
    'alex': [6, 2, 9],
    'colton': [56, 4],
    'jack': [13, 8, 1, 3],
    'donald': [62, 43],
    'eric': [8, 67, 23, 91, 79],
    }

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")