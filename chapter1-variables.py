_cars = 23
cars = 24

CARS = 25
CARS = 12345
CARS = 56789

number_of_cars = 23
kind_of_cars = "Ferrari"

print(cars)
print(_cars)
"""
Will print the last variable
if there is more than 1 similar variable
"""
print(CARS)
print(kind_of_cars)

"""
This is a multi-line comment
You can use this kind of comment to
make longer notes as you are learning.
In python, there are often used as 
docstrings.

You can also use (''' ''') to create 
multi-line comment.
"""

# This is single line comment

name = "Janelle Jones"
type_of_car = "Rolls royce"
school = "Foundation Elementary School"

print(name + school)
print(name + " " + school)
print(name + " works at " + school +".")
# python string.format()
print("{} works at {}.".format(name, school))