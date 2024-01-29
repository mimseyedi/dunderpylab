n = int(input(">>> "))
f = int(input(">>> "))

counter = 1
while counter < n:
    if counter % f == 0:
        print(counter)
    counter += 1