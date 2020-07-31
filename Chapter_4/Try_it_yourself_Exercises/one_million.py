# Radovan Novakovity
# Try it yourself 4-4.
#  Make a list of the numbers from one to one million, and then use a for loop to print the numbers
#  (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.) 

numbers = []
for value in range(1,1000000):
	numbers.append(value)

for number in numbers:
	print(number)