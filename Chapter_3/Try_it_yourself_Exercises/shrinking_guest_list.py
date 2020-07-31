# Radovan Novakovity
# Try it yourself 3-7.
#  Start with your program from Exercise 3-6
#  Add a new line that prints a message saying that you can invite only two people for dinner
#  Use pop() to remove guests from your list one at a time until only two names remain in your list
#  Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner
#  Print a message to each of the two people still on your list, letting them know they’re still invited
#  Use del to remove the last two names from your list, so you have an empty list
#  Print your list to make sure you actually have an empty list at the end of your program

# Part 3-6.
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

# Part 3-7.
sorry_message = "\nHey everbody, I'm sorry but change of plans. I can only invite two of you.\n"

print(sorry_message)

removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}, but I cannot invite you for dinner this time.")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}, but I cannot invite you for dinner this time.")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}, but I cannot invite you for dinner this time.")
removed_guest = guests.pop()
print(f"I'm sorry {removed_guest}, but I cannot invite you for dinner this time.")

print(f"\nHey {guests[0]}, you are still invited, you should come.")
print(f"Hey {guests[1]}, you are still invited, you should come.\n")

del guests[0]
del guests[0]
print(guests)