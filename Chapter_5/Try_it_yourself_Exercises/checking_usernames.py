# Radovan Novakovity
# Try it yourself 5-10.
#  Do the following to create a program that simulates how websites ensure that everyone has a unique username
#  Make a list of five or more usernames called current_users
#  Make another list of five usernames called new_users
#  Make sure one or two of the new usernames are also in the current_users list
#  Loop through the new_users list to see if each new username has already been used
#  If it has, print a message that the person will need to enter a new username
#  If a username has not been used, print a message saying that the username is available

current_users = ['John', 'Eric', 'Brandon', 'Colton', 'Alex']
new_users = ['Dusty', 'Max', 'Brandon', 'Steve', 'Eric']

current_users_lower = []

for user in current_users:
    current_user_lower = user.lower()
    current_users_lower.append(current_user_lower)
# current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("I'm sorry, but that username is already taken, please enter a new one")
    else:
        print("Good news, the username is available!")