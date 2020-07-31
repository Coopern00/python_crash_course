# Radovan Novakovity
# Try it yourself 8-13.
#  Start with a copy of user_profile.py
#  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you

# user_profile.py part
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             locacation='princeton',
                             field='physics')
print(user_profile)

# 8-13. parts
user_profile = build_profile('radovan', 'novakovity',
                             location='hungary',
                             field='IT',
                             hair_color='blonde',)

print(user_profile)