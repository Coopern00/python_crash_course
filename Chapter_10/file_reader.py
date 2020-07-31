# Reading an Entire File
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
# rstrip is for removing an emtpy string as a blank line which the read() method makes if it reaches the end of the file 
print(contents.rstrip())

# Telling python to look for the txt in a folder inside the folder where the .py file is stored using the relative file path
#  with open('text_files/filename.txt') as file object:

# Telling python to look for the txt in a folder which is not located inside of the folder where the .py file is stored using the absolute path
# It's easier to store the path in a variable
#  file_path = '/home/user/other_files/text_files/filename.txt'
#  with open(file_path) as file_object

# Reading Line by Line
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a File
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())