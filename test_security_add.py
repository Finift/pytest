import shutil


shutil.copyfile('securities.txt', 'sec_add.txt')

#Добавляем бумагу
with open('sec_add.txt', mode='a') as sec_add:
    sec_add.write('BBG000B9Y9C7')
#сравнение содержимого файлов
data1 = open('securities.txt', 'r').readlines()
data2 = open('sec_add.txt', 'r').readlines()
output = []
for item in data2:
    if item not in data1:
        output.append(item)


def test_comparison():
    assert 'BBG000B9Y9C7' in output, "Item wasn't added"
#
# #Удаление всех данных из файла:
# f = open('sec_add.txt', 'r+')
# # absolute file positioning
# f.seek(0)
# # to erase all data
# f.truncate()
