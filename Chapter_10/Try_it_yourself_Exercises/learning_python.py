# Radovan Novakovity
# Try it yourself 10-1.
#  Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far
#  Start each line with the phrase In Python you can. . . .
#  Save the file as learning_python.txt in the same directory as your exercises from this chapter
#  Write a program that reads the file and prints what you wrote three times
#  Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block

# Storing the text file in a variable for easier use
filename = 'learning_python.txt'

# Opening the text file and storing it in the file_object variable
with open(filename) as file_object:
    # Looping over the file object and printing them
    for line in file_object:
        print(line.rstrip())

print("\n")

# Opening the text file and storing it in the file_object variable
with open(filename) as file_object:
    # Starting to store each line in a list from the text file to be able to use the data outside of this code block
    lines = file_object.readlines()

# Creating an empty string to
learning_string = ''
for line in lines:
    # Adding each line from the list to the string variable
    learning_string += line

print(f"{learning_string}")