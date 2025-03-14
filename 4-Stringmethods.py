#string methods in python
course = "   python for beginners    "
#upper method converts the string to uppercase. it does not modify the original string
print(course.upper())
#lower method converts the string to lowercase. it does not modify the original string
print(course.lower())
#title method converts the first character of each word to uppercase. it does not modify the original string
print(course.title())
#strip method removes any whitespace at the beginning or end. it does not modify the original string
print(course.strip())
#lstrip method removes any whitespace at the beginning. it does not modify the original string
print(course.lstrip())
#rstrip method removes any whitespace at the end. it does not modify the original string
print(course.rstrip())
#find method returns the index of the first occurrence of the specified value. it returns -1 if the value is not found
print(course.find("be"))
#replace method replaces a string with another string. it does not modify the original string
print(course.replace("p","j"))
#in operator returns true if the specified value is found in the string
print("begi" in course)
#not in operator returns true if the specified value is not found in the string
print("z" not in course)
#string methods are chainable
print(course.upper().strip())
#string methods are chainable
print(course.upper().strip().replace("P","J"))