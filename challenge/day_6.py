# Write a function called user_name that 
# generates a username from the user’s email. 
# The code should ask the user to input an email 
# and the code should return everything before 
# the @ sign as their user name. 
# For example, if someone enters ben@gmail.com, 
# the code should return ben as their user name.

def user_name(email):
    name_gen = email.split('@')
    return name_gen[0]

print('Username:', user_name(input('Email: ')))



# Write a function called zeroed code that takes 
# a list of numbers as an argument. 
# The code should zero (0) the 
# first and the last number in the list. 
# For example, if the input is [2, 5, 7, 8, 9],
# your code should return [0, 5, 7, 8, 0].

data = [2, 5, 7, 8, 9]

def zeroed(data):
    data = map(data.replace())