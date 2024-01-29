user_input = int(input(">>> "))
counter, s = 1, 0

while counter <= user_input:
    s += counter
    counter += 1

print(s)
