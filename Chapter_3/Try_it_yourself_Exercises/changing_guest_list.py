# Radovan Novakovity
# Try it yourself 3-5.
#  You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations
#  You'll have to think of someone else to invite
#  Start with your program from Exercise 3-4
#  Add a print() call at the end of your program stating the name of the guest who can't make it
#  Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting
#  Print a second set of invitation messages, one for each person who is still in your list

# From 3-4.
guests = ['Brandon', 'Erik', 'Colton']

message_one = f"Hello {guests[0]}, I would like to invite you for dinner."
message_two = f"Hello {guests[1]}, I would like to invite you for dinner."
message_three = f"Hello {guests[2]}, I would like to invite you for dinner."

print(message_one)
print(message_two)
print(message_three)

# 3-5. part
message_four = f"\n{guests[2]} can't make it for dinner.\n"

print(message_four)

del guests[2]
guests.append('Alex')
message_three = f"Hello {guests[2]}, I would like to invite you for dinner."

print(message_one)
print(message_two)
print(message_three) 