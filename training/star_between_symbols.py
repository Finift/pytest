# Дана строка. Получите новую строку, вставив между каждыми двумя символами
# исходной строки символ *. Выведите полученную строку.
# без последней звездочки)
text = input()
text = list(text)
text2 = []
for i in text:
    text2.append(i)
    text2.append('*')
text2.pop()
text = ''.join(text2)
print(text)
