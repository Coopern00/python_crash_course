# Radovan Novakovity
# Try it yourself 6-3.
#  A Python dictionary can be used to model an actual dictionary
#  However, to avoid confusion, let’s call it a glossary
#  Think of five programming words you’ve learned about in the previous chapters
#  Use these words as the keys in your glossary, and store their meanings as values
#  Print each word and its meaning as neatly formatted output
#  You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line
#  Use the newline character (\n) to insert a blank line between each word-meaning pair in your output

programming_words = {
    'Tuple': 'Python refers to values that cannot change as immutable, an an immutable list is called a tuple.',
    'Boolean': 'A Boolean value is either True or Flase, just like the value of a conditional expression.',
    'List': 'A list is a collection of items in a particular order.',
    'Comment': 'A comment allows you to write notes in English within your programs.',
    'String': 'A string is simply a series of characters.',
    }

word = 'Tuple'
print(f"{word}: {programming_words['Tuple']}")

word = 'Boolean'
print(f"\n{word}: {programming_words['Boolean']}")

word = 'List'
print(f"\n{word}: {programming_words['List']}")

word = 'Comment'
print(f"\n{word}: {programming_words['Comment']}")

word = 'String'
print(f"\n{word}: {programming_words['String']}")