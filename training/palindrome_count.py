k = int(input())

if 1 > k or k > 100000:
    print("k error")
else:
    palindrome_count = 0
    for i in range(1, (k + 1)):
        i = str(i)
        i_reverse = i[::-1]
        if i == i_reverse:
            palindrome_count += 1
    print(palindrome_count)
