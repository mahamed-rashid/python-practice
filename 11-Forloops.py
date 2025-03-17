# For loops are used to iterate over a sequence (a list, a tuple, a dictionary, a set, or a string).
# Syntax:
# for item in sequence:
for number in range(3):
    print("Attempt", number)
print("---------------------")
# adding +1 to the number
for number in range(3):
    print("Attempt", number + 1)
print("---------------------")
for number in range(3):
    print("Attempt", number + 1, (number+1)*".")
print("---------------------")
# passing the range function with 1 and 4 as arguments
for number in range(1, 4):
    print("attempt", number)
print("---------------------")
# passing step as 2
for number in range(1, 10, 3):
    print("attempt", number, number*".")

# for..else loop
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Attempted 3 times and failed")
