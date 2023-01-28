l1, r1, l2, r2, l3, r3 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
if 0 <= l1 < r1 <= 100 or 0 <= l2 < r2 <= 100 or 0 <= l3 < r3 <= 100:
    if l2 <= r1:
        if l3 <= r2 or l3 <= r1:
            print(0)
        elif (l3 - r2) > (r1 - l1):
            print(3)
        else:
            print(1)
    if l2 > r1:
        if l3 <= r2:
            print(1)
        else:
            if (l3 - r2) <= (r1 - l1):
                print(1)
            else:
                if (l2 - r1) <= (r3 - l3):
                    print(3)
                else:
                    print(-1)
else:
    print(-1)
