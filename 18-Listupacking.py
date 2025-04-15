#list unpacking is a way to assign values from a list to variables.
#first and last is unpacked from the list and other is packed into a list
numbers = [1,2,3,4,5,6,7,8,9,10]
first, *other, last = numbers
print(first, last)
print(other)

# looping over a list
# to get thhe index value we can use the enumerate function which is iterable. the result will be like this (0,1)(0,2) in tuple format.
#we can unpack the tuple into two variables and tuples are read only(immutable)
for index, number in enumerate(numbers):
    print(index, number)

#adding and removing elements from a list

#to add an item at the end
numbers.append(11)
print(numbers)
#to add at particular index
numbers.insert(0,0)
print(numbers)

#to remove an item we have pop. pop is used to remove the last item from the list. we can also pass the index of the item to be removed.
numbers.pop(0)
print(numbers)
#to remove a particular item we can use remove
numbers.remove(11)
print(numbers)

#to remove all items from the list we can use del. we del to remove range of items
del numbers[0:-1]
print(numbers)

#to remove all items from the list we can use clear
numbers.clear()
print(numbers)

# finding items in a list

letters = ['a', 'b', 'c', 'd', 'e','e','a']
print(letters.index('a'))
#print index of an item that does not exist will throw an error in python
#print(letters.index('f')) #will throw an error

#to check the how many times an item occurs in a list we can use count
print(letters.count('e'))

