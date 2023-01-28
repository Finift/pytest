a = []
b = int(input())
while b != 0:
    a.append(b)
    b = int(input())

prev = a[0]
H_counter = 1
D_counter = 1
c = []
for i in a:
    if i != prev:
        if i > prev:
            D_counter = 1
            H_counter += 1
            c.append(H_counter)
            prev = i
        else:
            H_counter = 1
            D_counter += 1
            c.append(D_counter)
            prev = i

    else:
        D_counter = H_counter = 1
        prev = i
        c.append(1)
print(max(c))
