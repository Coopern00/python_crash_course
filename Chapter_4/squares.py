# Using range() to make a list of numbers
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print(squares)

print("\n")

squares = []
for value in range(1, 11):
	squares.append(value**2)

print(squares)

print("\n")

# List comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)