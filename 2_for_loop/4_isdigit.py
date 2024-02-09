user_input = input(">>> ")

for char in user_input:
    if char not in '0123456789':
        print(False)
        break
else:
    print(True)


# Using the 'isdigit()' method of the string class:
print(user_input.isdigit())