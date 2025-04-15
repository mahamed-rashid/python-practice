letters = ['a', 'b', 'c']
matrix = [[0,1],[2,3]]
zeros = [0] * 5
combined = zeros + letters
print(combined)
numbers = list(range(20))
print(numbers)
chars = list("Hi there")
print(len(chars))

#accessing list

numbers = list(range(20))
print(numbers[0])
print(numbers[-1])
print(numbers[0:3])
print(numbers[:3])
print(numbers[:])
print(numbers[::2])  # every second element
print(numbers[::1])  # every element
print(numbers[::-1])  # reverse the list