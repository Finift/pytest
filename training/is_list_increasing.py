def IsAscending(A):
    if len(A) == 1:
        return True
    else:
        a = 0
        while a in range(len(A)-1) and A[a] < A[a+1]:
            a += 1
        if a == (len(A) - 1):
            return True
        else:
            return False


A = list(map(int, input().split()))
if IsAscending(A):
    print('YES')
else:
    print('NO')
