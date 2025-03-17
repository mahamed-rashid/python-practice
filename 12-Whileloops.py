# while loop is used to execute a block of statements repeatedly until a given condition is true.
#we have to define a command variable because without that while doesn't knwo what command is.
command = ""
#the lower() method converts the string to lowercase. So we don't have add mutiple conditions for the user to quit the program.
while command.lower() != "quit":
    command = input(">")
    print("Echo", command)
#infinite loop
# while True:
#     command = input(">")
#     print("Echo", command)
#     if command.lower() == "quit":
#         break