def greet(first_name, last_name):  # parameters
    print(f"Hi {first_name} {last_name}")
    print("Welcome to the python course")


greet("John", "Smith")  # arguments
# we have two types of functions in python
# 1. Perform a task
# 2. Calculate and return a value
# In python bydefault the function returns None. We can return a value using the return keyword.


def get_greeting(name):
    return f"Hi {name}"


# we can also store the return value in a variable. it is useful when we want to use the return value later in the program
print(get_greeting("John"))

# keyword arguments
# we can specify the name of the argument when calling the function. it makes the code more readable
# we can also change the order of the arguments


def increment(number, by):
    return number + by


print(increment(2, by=1))

# default arguments. we can specify the default value for the argument. if the argument is not passed, the default value is used
# the default argument should be the last argument. we cannot have a default argument before a non-default argument


def increment_one(number, by=1):
    return number + by


print(increment_one(2))
