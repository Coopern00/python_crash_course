# Radovan Novakovity
# Try it yourself 8-7.
#  Write a function called make_album() that builds a dictionary describing a music album
#  The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information
#  Use the function to make three dictionaries representing different albums
#  Print each return value to show that the dictionaries are storing the album information correctly
#  Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album
#  If the calling line includes a value for the number of songs, add that value to the album’s dictionary
#  Make at least one new function call that includes the number of songs on an album

# Making a function that takes two paramaters, and an optional one
def make_album(artist_name, album_title, track_number=0):
    """Return a dictionary of information about artists and their albums"""
    album = {
        'artist': artist_name.title(),
        'album': album_title.title(),
        }
    if track_number:
        album['track_number'] = track_number
    return album

# Making three dictionaries, then printing them to see if the information was stored properly
album = make_album('artist_one', 'album_one')
print(album)

album = make_album('artist_two', 'album_two')
print(album)

album = make_album('artist_three', 'album_three')
print(album)

# Making a third dictionary with an optional track_number parameter
album = make_album('artist_four', 'album_four', 3)
print(album)