user_input = input(">>> ")

counter = 1
for char in user_input:
    print(counter, char)
    counter += 1


# Using built-in 'enumerate()':
for index, char in enumerate(user_input):
    print(index, char)