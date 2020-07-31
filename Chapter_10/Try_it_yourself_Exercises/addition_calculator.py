# Radovan Novakovity
# Try it yourself 10-7.
# Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number

def number_sum(input_number_one, input_number_two):
    """This function is for adding two numbers together"""
    try:
        result = int(input_number_one) + int(input_number_two)
    except ValueError:
        print("Please enter the numbers numerically.")
    else:
        print(f"The sum of these numbers are: {result}")

print("Hello, in order to add two numbers, please enter the desired numbers")
print("In order to quit simply write 'q'")

while True:
    prompt_one = input("First number: ")
    # If the users enters q then the while loop stops
    if prompt_one == 'q':
        break
    prompt_two = input("Second number: ")
    # If the users enters q then the while loop stops
    if prompt_two == 'q':
        break

    number_sum(prompt_one, prompt_two)