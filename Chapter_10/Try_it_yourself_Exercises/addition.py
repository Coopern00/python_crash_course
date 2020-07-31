# Radovan Novakovity
# Try it yourself 10-6.
#  One common problem when prompting for numerical input occurs when people provide text instead of numbers
#  When you try to convert the input to an int, you’ll get a ValueError
#  Write a program that prompts for two numbers
#  Add them together and print the result
#  Catch the ValueError if either input value is not a number, and print a friendly error message
#  Test your program by entering two numbers and then by entering some text instead of a number

def number_sum(input_number_one, input_number_two):
    """This function is for adding two numbers together"""
    try:
        result = int(input_number_one) + int(input_number_two)
    except ValueError:
        print("Please enter the numbers numerically.")
    else:
        print(f"The sum of these numbers are: {result}")

print("Hello, in order to add two numbers, please enter the desired numbers")

prompt_one = input("First number: ")
prompt_two = input("Second number: ")
number_sum(prompt_one, prompt_two)