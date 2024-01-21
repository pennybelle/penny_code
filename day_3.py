# Write a function called register_check that checks how many students are in school.
# The function takes a dictionary as a parameter. 
# If the student is in school, the dictionary says ‘yes’. 
# If the student is not in school, the dictionary says ‘no’. 
# Your function should return the number of students in school. 
# Use the dictionary below. Your function should return 3.

data = {'Michael' : 'yes', 'John' : 'no' , 'Peter' : 'Yes', 'Mary': 'Yes'}

def register_check(data):
    enrolled = 0
    for student in data:
        if str(data[student]).casefold() == 'yes':
            enrolled += 1
    return enrolled

print(register_check(data))

# You are given a list of names above. 
# This list is made up of names of lowercase and uppercase letters. 
# Your task is to write a code that will return a tuple of all the 
# names in the list that have only lowercase letters. 
# Your tuple should have names sorted alphabetically in descending order. 
# Using the list above, your code should return:
# ('kerry', 'dickson', 'carol', 'adam')

names = ['kerry', 'dickson', 'joHN', 'Mary', 'carol', 'Rose', 'adam']

def if_lowercase(data):
    is_lower = []
    for item in data:
        if item.casefold() == item:
            is_lower.append(item)
    return tuple(is_lower)

print(if_lowercase(names))

# def if_lowercase(data):
#     var = map(lambda x: x.lower(), data)
#     return var

# print(if_lowercase(names))

# ascii = []
# for ascii in range(1, 100):
#     ascii += 

def lower_names(data):
    all_lower = [item for item in data if item.islower()]
    return all_lower

print(lower_names(names))