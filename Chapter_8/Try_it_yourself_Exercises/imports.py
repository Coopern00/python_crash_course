# Radovan Novakovity
# Try it yourself 8-16.
#  Using a program you wrote that has one function in it, store that function in a separate file. 
#  Import the function into your main program file, and call the function using each of these approaches:
#   import module_name 
#   from module_name import function_name 
#   from module_name import function_name as fn 
#   import module_name as mn
#   from module_name import *


# import profile_build
# from profile_build import build_profile
# from profile_build import build_profile as bf
# import profile_build as bf
from profile_build import *

user_profile = build_profile('albert', 'einstein',
                             locacation='princeton',
                             field='physics')
print(user_profile)