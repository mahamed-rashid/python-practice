# xargs is a keyword that allows you to pass a variable number of arguments to a function
# *args is a tuple of the arguments passed to the function
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# **kwargs is a dictionary of the keyword arguments passed to the function


def save_user(**user):
    print(user)  # user is a dictionary object
    print(user["id"])
    print(user["name"])
    print(user["age"])


save_user(id=1, name="John", age=22)
