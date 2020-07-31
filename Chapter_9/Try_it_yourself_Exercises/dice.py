# Radovan Novakovity
# Try it yourself 9-13.
#  Make a class Die with one attribute called sides, which has a default value of 6
#  Write a method called roll_die() that prints a random number between 1 and the number of sides the die has
#  Make a 6-sided die and roll it 10 times
#  Make a 10-sided die and a 20-sided die. Roll each die 10 times

# Importing the random module
from random import randint

# Making the Die class with attribute
class Die():
    """This class represent a die."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    # Making the method for rolling the dice for a random number between 1 and the given side number
    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

# Creating an instance of the Die with 6 sides
first_die = Die()
# Making 10 rolls using the method, storing it in a list, then printing the results
results = []
for roll_num in range(10):
    result = first_die.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Creating an instance of the Die with 10 sides
second_die = Die(10)
# Making 10 rolls using the method, storing it in a list, then printing the results
results = []
for roll_num in range(10):
    result = first_die.roll_die()
    results.append(result)
print("10 rolls of a 10-sided die:")
print(results)

# Creating an instance of the Die with 20 sides
first_die = Die(20)
# Making 10 rolls using the method, storing it in a list, then printing the results
results = []
for roll_num in range(10):
    result = first_die.roll_die()
    results.append(result)
print("10 rolls of a 20-sided die:")
print(results)