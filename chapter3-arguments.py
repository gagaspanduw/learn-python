# Positional arguments
def user_info(name, age, city):
    '''This function prints name, age, and city
    from an arguments provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info("Janet", 58, "Oklahoma City")
# will error because missing 1 argument
# user_info(34, "New York")

# Keyword arguments
def user_info1(name, age=0, city="Tucson"):
    '''This function prints name, age, and city
    from an arguments provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info1("Micah")
user_info1(age=56, name="Kadeem")