# Radovan Novakovity
# Try it yourself 3-6.
#  You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner
#  Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table
#  Use insert() to add one new guest to the beginning of your list
#  Use insert() to add one new guest to the middle of your list
#  Use append() to add one new guest to the end of your list
#  Print a new set of invitation messages, one for each person in your list

guests = ['Brandon', 'Erik', 'Colton']

message_one = f"Hello {guests[0]}, I would like to invite you for dinner."
message_two = f"Hello {guests[1]}, I would like to invite you for dinner."
message_three = f"Hello {guests[2]}, I would like to invite you for dinner."

print(message_one)
print(message_two)
print(message_three)

message_announcement = "\nGood news everyone! I have found a bigger dinner table.\n"

print(message_announcement)

guests.insert(0, 'Caleb')
guests.insert(2, 'Alex')
guests.append('Jon')

message_one = f"Hello {guests[0]}, I would like to invite you for dinner."
message_two = f"Hello {guests[1]}, I would like to invite you for dinner."
message_three = f"Hello {guests[2]}, I would like to invite you for dinner."
message_four = f"Hello {guests[3]}, I would like to invite you for dinner."
message_five = f"Hello {guests[4]}, I would like to invite you for dinner."
message_six = f"Hello {guests[5]}, I would like to invite your for dinner."

print(message_one)
print(message_two)
print(message_three)
print(message_four)
print(message_five)
print(message_six)