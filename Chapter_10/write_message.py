# Writing to an Empty File
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")


# Writing Multiple Lines
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")


# Appending to a file
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")