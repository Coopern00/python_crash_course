# Radovan Novakovity
# Try it yourself 10-8.
#  Make two files, cats.txt and dogs.txt
#  Store at least three names of cats in the first file and three names of dogs in the second file
#  Write a program that tries to read these files and print the contents of the file to the screen
#  Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing
#  Move one of the files to a different location on your system, and make sure the code in the except block executes properly

filenames = ['cats.txt', 'dogs.txt']

# Iterating through the text files
for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            print(contents)
    # If the text file does not exist it prints an error message
    except FileNotFoundError:
        print(f"The file {filename} does not exist")