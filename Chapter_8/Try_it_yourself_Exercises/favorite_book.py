# Radovan Novakovity
# Try it yourself 8-2.
#  Write a function called favorite_book() that accepts one parameter, title
#  The function should print a message, such as "One of my favorite books is Alice in Wonderland"
#  Call the function, making sure to include a book title as an argument in the function call

def favorite_book(book_title):
    """This displays the title of a book."""
    print(f"One of my favorite book is {book_title.title()}.")

favorite_book('the hobbit')