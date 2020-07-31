# Radovan Novakovity
# Try it yourself 4-10.
#  Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following
#  Print the message "The first three items in the list are:"
#  Then use a slice to print the first three items from that program’s list
#  Print the message "Three items from the middle of the list are:"
#  Use a slice to print three items from the middle of the list
#  Print the message "The last three items in the list are:"
#  Use a slice to print the last three items in the list

# Try it yourself 4-6. part
odd_numbers = list(range(1,21,2))

for number in odd_numbers:
	print(number)

print("\n")

# Try it yourself 4-10. part
print("The first three items in the list are:")
print(odd_numbers[:3])

print("\n")

print("Three items from the middle of the list are:")
print(odd_numbers[3:6])

print("\n")

print("The last three items in the list are:")
print(odd_numbers[-3:])