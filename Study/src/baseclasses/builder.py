

class BuilderBaseClass:
    def __init__(self):
        self.result = {}

    # Для обновления любого значения, в т.ч. вложенного
    # пример, на который мы это и пишем:
    # player = {
    #     "account_status": "active",
    #     "balance": 10,
    #     "localize": {
    #         "en": {"nickname": "Solve", "countries": {"UA": 3}, {"ennn": {"abc": 5}}}
    #     }
    # }

    def update_inner_value(self, keys, value):
        if not isinstance(keys, list):  # Для обновления параметров верхнего уровня, не вложенных
            self.result[key] = value
        else:
            temp = self.result
            for i in keys[:-1]:  # исключили последний элемент из перебора, чтобы именно ему присвоить значение
                if i not in temp.keys():
                    temp[i] = {}  # если такого нет, создадим и зайдем в него сл.шагом
                temp = temp[i]  # зашли в локалайз
            temp[keys[-1]] = value
        return self

# Выход из билдера после всех нужных изменений:
    def build(self):
        return self.result