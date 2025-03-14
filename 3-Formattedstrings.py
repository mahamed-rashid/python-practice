#formatted string is a way to embed variables inside a string. it starts with f and then {variable}
first = "John"
last = "Smith"
#traditional way of concatenating strings
full = first + " "+ last
print(full)
#formatted string. we can use string functions inside the curly braces like len, upper, lower, etc
full = f"formatted string: {first} {last}"
print(full)