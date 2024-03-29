from Study.src.enums.user_enums import Statuses
from Study.src.generators.player_localization import PlayerLocalization
from Study.src.baseclasses.builder import BuilderBaseClass


class Player(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.reset()  # - при использовании ресета, наполним массив дефолтными значениями, бнез него массив будет пустым

    def set_status(self, status=Statuses.active.value):
        self.result['account status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar="https://google.com/"):
        self.result['avatar'] = avatar

    # наполняем массив данными
    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result["localize"] = {
            "en": PlayerLocalization('en_US').build(),
            "ru": PlayerLocalization('ru_RU').build()
        }
        return self

    # Обновили локализацию, теперь вместо тех двух эта одна
    def update_inner_generator(self, key, generator):
        self.result[key] = {'fr': generator.build()}
        return self



z = Player().build()
z = Player().set_balance(20).build()  # изменили балланс с 0 на 20
print(z)
