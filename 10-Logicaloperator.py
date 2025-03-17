# we have three logical operators in python and, or and not. and operator returns true if both operands are true. or operator returns true if at least one of the operands is true. not operator returns the opposite of the operand.
high_income = False
good_credit = True
student = False
if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")
if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")
if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not Eligible")

# Chaining comparison operators
# we can chain comparison operators in python. for example, we can use the and operator to combine two comparison operators. the below code checks if the price is between 10 and 30.
age = 22
if 18 <= age < 65:
    print("Eligible")
else:
    print("Not Eligible")
