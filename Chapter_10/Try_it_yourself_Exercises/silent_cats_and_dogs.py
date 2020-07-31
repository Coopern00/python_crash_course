# Radovan Novakovity
# Try it yourself 10-9.
#  Modify your except block in Exercise 10-8 to fail silently if either file is missing

filenames = ['cats.txt', 'dogs.txt']

# Iterating through the text files
for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            print(contents)
    # If the text file does not exist it prints an error message
    except FileNotFoundError:
        pass