y = 0
for x in range(1, 10):
    # better way
    if x % 2 == 0:
        y += 1
        print(x)
#    remainder = x % 2
#    if remainder == 0:
print(f"we have {y} even numbers")
