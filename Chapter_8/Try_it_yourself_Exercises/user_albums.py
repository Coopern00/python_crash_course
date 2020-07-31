# Radovan Novakovity
# Try it yourself 8-8.
#  Start with your program from Exercise 8-7
#  Write a while loop that allows users to enter an album’s artist and title
#  Once you have that information, call make_album() with the user’s input and print the dictionary that’s created
#  Be sure to include a quit value in the while loop

# Making a function that takes two paramaters, and an optional one
def make_album(artist_name, album_title, track_number=0):
    """Return a dictionary of information about artists and their albums"""
    album = {
        'artist': artist_name,
        'album': album_title,
        }
    if track_number:
        album['track_number'] = track_number
    return album

# Making a while loop to take a users input
while True:
    print("If you would like to quit this application, simply write 'quit' to do so")
    artist = input("Please enter the name of the artist: ")
    # Making sure that the user has an option to quit avoiding an endless loop
    if artist == 'quit':
        break

    album = input("Please enter the name of the album: ")
    # Making sure that the user has an option to quit avoiding an endless loop
    if album == 'quit':
        break

    artist_album = make_album(artist, album)
    print(artist_album)