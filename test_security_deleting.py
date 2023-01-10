with open('securities.txt', mode='r') as sec_list:
    data = sec_list.readlines()
    item_for_del = list(data)[3]
    item_for_del = str(item_for_del)

with open('securities.txt', mode='w') as sec_list:
    for line in data:
        if line != item_for_del:
            sec_list.write(line)

with open('securities.txt', mode='r') as sec_list:
    data = sec_list.readlines()

def test_sec_del():
    assert item_for_del not in data, 'Security was not delete.'

with open('securities.txt', mode='a') as sec_list:
    sec_list.write(item_for_del)
