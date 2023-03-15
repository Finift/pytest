import shutil


shutil.copyfile('securities.txt', 'sec_add.txt')

#Добавляем бумагу
with open('sec_add.txt', mode='a') as sec_add:
    sec_add.write('BBG000B9Y9C7')
#сравнение содержимого файлов для построчного сравнения
# data1 = open('securities.txt', 'r').readlines()
# data2 = open('sec_add.txt', 'r').readlines()
# output = []
# for item in data2:
#     if item not in data1:
#         output.append(item)


#Просто проверка, что файл добавлен
def test_comparison():
    data = open('sec_add.txt', 'r').readlines()
    assert 'BBG000B9Y9C7' in data, "Item wasn't added"
    sec_add.close()
#
# #Удаление всех данных из файла:
# f = open('sec_add.txt', 'r+')
# # absolute file positioning
# f.seek(0)
# # to erase all data
# f.truncate()
