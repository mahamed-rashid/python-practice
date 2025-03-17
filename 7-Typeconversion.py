# In python the user input is always a string. To convert the string to a number, we can use the int function. Likewise we have float function to convert the string to a floating point number and bool function to convert the string to a boolean value. str function converts the number to a string.
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

#bool false values: "", 0, None
#bool true values: any other value