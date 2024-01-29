n = int(input(">>> "))
f = int(input(">>> "))

counter = 0
while counter < n:
    counter += 1
    if counter % f == 0:
        continue
    print(counter)
