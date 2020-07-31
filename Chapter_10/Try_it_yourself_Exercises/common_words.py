# Radovan Novakovity
# Try it yourself 10-10.
#  Visit Project Gutenberg (https://gutenberg.org/ ) and find a few texts you’d like to analyze
#  Download the text files for these works, or copy the raw text from your browser into a text file on your computer
#  You can use the count() method to find out how many times a word or phrase appears in a string
#  For example, the following code counts the number of times 'row' appears in a string
#   line = "Row, row, row your boat"
#   line.count('row')
#   line.lower().count('row') 
#  Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for, regardless of how it’s formatted
#  Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text
#  This will be an approximation because it will also count words such as 'then' and 'there'
#  Try counting 'the ', with a space in the string, and see how much lower your count is

def word_count(filename):
    """This function counts how many times does the word 'the' appears in a text"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            # This is for counting 'the' without whitespace
            #count = int(contents.lower().count('the'))
            # This is for counting 'the ' with whitespace
            count = contents.lower().count('the ')
    except FileNotFoundError:
        print(f"The file named {filename} does not exist.")
    else:
        print(f"The word 'the' appears {count} times in {filename}")

filenames = [
    'a_half_century_of_conflict.txt',
    'hafbur_and_signe_a_ballad.txt',
    'the_race_of_the_swift.txt',
    ]

for filename in filenames:
    word_count(filename)