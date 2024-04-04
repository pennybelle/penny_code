# Create a function called my_discount. 
# The function takes no arguments but asks the user to input 
# the price and the discount (percentage) of the product. 
# Once the user inputs the price and discount, 
# it calculates the price after the discount. 
# The function should return the price after the discount. 
# For example, if the user enters 150 as price and 
# 15% as the discount, your function should return 127.5.

# this solution doesnt seem super elegant 
def my_discount():
    price = int(input('Price: ').replace('$', ''))
    discount = int(input('Discount: ').replace('%', ''))
    return price - ((discount / 100) * price)

print(my_discount())



# You work for a school and your boss wants to know how many
# female and male students are enrolled in the school.
# The school has saved the students in a list. 
# Your task is to write a code that will count how many 
# males and females are in the list. Here is a list below:

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

# Your code should return a list of tuples. The list above should return:
# [(‘Male’,7), (‘female’,6)]

# i dont like this one either but it works
def student_bodies(students):
    student_sexes = [
        ('Male', len([s for s in students if s.lower() == 'male'])),
        ('female', len([s for s in students if s.lower() == 'female']))
    ]
    return student_sexes

print(student_bodies(students))