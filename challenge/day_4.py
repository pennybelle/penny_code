# Write a function called only_floats, which takes two parameters a and b, 
# and returns 2 if both arguments are floats, returns 1 if only one argument 
# is a float, and returns 0 if neither argument is a float. 
# If you pass (12.1, 23) as an argument, your function should return a 1.

a, b = 12.1, 23

# def only_floats(a, b):
#     total_floats = 0
#     for item in a, b:
#         if type(item) is float:
#             total_floats += 1
#     return total_floats

# def only_floats(a, b):
#     total_floats = [n for n in (a, b) if isinstance(n, float)]
#     return len(total_floats)

# def only_floats(a, b):
#     total_floats = [n for n in (a, b) if type(n) is float]
#     return len(total_floats)

# I LOVE THIS
def only_floats(*data):
    return sum(type(x) is float for x in data)

print(only_floats(a, b))



# Write a function called word_index that takes one argument, 
# a list of strings and returns the index of the longest word in the list. 
# If there is no longest word (if all the strings are of the same length), 
# the function should return zero (0). 

# For example, the list below should return 2.
words1 = ["Hate", "remorse", "vengeance"] 

# And this list below, shoul return zero (0) 
words2 = ["Love", "Hate"]

def word_index(data):
    longest_word = max(data, key = len)
    return data.index(longest_word)

print(word_index(words1))
print(word_index(words2))