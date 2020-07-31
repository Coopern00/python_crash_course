# Radovan Novakovity
# Try it yourself 6-4.
#  Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values
#  When you’re sure that your loop works, add five more Python terms to your glossary
#  When you run your program again, these new words and meanings should automatically be included in the output

glossary = {
    'Tuple': 'Python refers to values that cannot change as immutable, an an immutable list is called a tuple.',
    'Boolean': 'A Boolean value is either True or Flase, just like the value of a conditional expression.',
    'List': 'A list is a collection of items in a particular order.',
    'Comment': 'A comment allows you to write notes in English within your programs.',
    'String': 'A string is simply a series of characters.',
    'Variable': 'Every variable hold a value, which is the information associated with that variable.',
    'Concatenation': 'The method of combining strings.',
    'Whitespace': 'Refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols.',
    'Syntax error': 'It occurs when Python doesnt recognize a section of your program as valid Python code',
    'Float': 'Python calls any number with a decimal point a float.',
    }

for word, value in glossary.items():
    print(f"{word}: {value}\n")