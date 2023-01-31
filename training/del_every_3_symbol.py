# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
# # Символы строки нумеруются, начиная с нуля.
# text = input()
# text = list(text)
# text2 = []
# for i in range(len(text)):
#     if i % 3 != 0:
#         text2.append(text[i])
# text = ''.join(text2)
# print(text)

# или:
# s = input()
# k = ' '.join(s).split(' ')
# del k[::3]
# print(''.join(k))

# чтение из файла и запись в другой:
s = open("string.txt", 'r')
string = s.read()
k = ' '.join(string).split(' ')
del k[::3]
outfile = open('output.txt', 'w')
print(''.join(k), file=outfile)
