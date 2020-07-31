# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

# In this Python automatically starts the slice at the beginning of the list
print(players[:4])

# In this Python slice the last part of the list from index 2
print(players[2:])

# This prints the names of the last three players
print(players[-3:])

print("\n")

# Looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())