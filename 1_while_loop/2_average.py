n, s = 0, 0

while True:
    user_input = input(">>> ")
    if user_input == 'done':
        print(s / n)
        break
    s += int(user_input)
    n += 1