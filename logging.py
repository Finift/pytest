import sys
from Lib import logging

# add filemode="w" to overwrite, по умолчанию стоит "a" - append
#logging.basicConfig(filename="logi.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(funcName)s %(processName)s %(lineno)d %(message)s")
# Будут писаться все уровни логов, начиная с Инфо, debug игнорится

# logging.debug("This is a debug message")
# logging.info("Informational message")
# logging.error("An error has happened!", exc_info=True) # exc_info=True - добавляет нам стек-трейс
# log = logging.getLogger("ex")

# try:
#     raise RuntimeError
# except RuntimeError:
#     log.exception("Error!")


# получение пользовательского логгера и установка уровня логирования
# py_logger = logging.getLogger(__name__)
# py_logger.setLevel(logging.INFO)
#
# # настройка обработчика и форматировщика в соответствии с нашими нуждами
# py_handler = logging.FileHandler(f"{__name__}.log", mode='w')
# py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(funcName)s %(processName)s %(lineno)d %(message)s")
#
# # добавление форматировщика к обработчику
# py_handler.setFormatter(py_formatter)
# # добавление обработчика к логгеру
# py_logger.addHandler(py_handler)

logging.basicConfig(filename="logi.log", format="%(asctime)s %(levelname)s %(funcName)s %(processName)s %(lineno)d %(message)s",
                        level=logging.INFO)


def lagrange(n):
    if n >= 10000:
        logging.error('so big integer', exc_info=True)
        sys.exit()
    else:
        logging.info(f'n = {n}')
        nw = n
        answ = []
        sc = int((n ** 0.5) // 1)
        if sc ** 2 == n:
            answ.append(sc)
            return answ
        else:
            for i in range(sc):
                c = sc - i
                k = 0
                n = nw
                answ = [c]
                while k < 3:
                    k += 1
                    n = n - (c ** 2)
                    c = int((n ** 0.5) // 1)
                    answ.append(c)
                    if c ** 2 == n:
                        return answ

try:
    n = int(input())
    logging.info("Process started")
except ValueError:
    logging.exception("It's NO int", exc_info=True)
    sys.exit()
print(*lagrange(n))
logging.info("Process finished")
sys.exit()
