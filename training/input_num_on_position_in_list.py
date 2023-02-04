def insert_num(a, pos, num):
    for i in range(len(a)+1):
        if i >= pos:
            i += 1
            a[i] = num
        return a


a = input().split()
b = input().split()
pos = int(b[0])
num = int(b[1])
print(*insert_num(a, pos, num))
