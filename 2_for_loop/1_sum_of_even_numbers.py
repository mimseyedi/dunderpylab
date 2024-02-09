user_input = int(input(">>> "))

s = 0
for even_number in range(2, user_input, 2):
    s += even_number

print(s)


# Using built-in 'sum()':
print(sum(range(2, user_input, 2)))