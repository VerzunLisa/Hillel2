# Написати декоратор до 2-х будь-яких функцій, який би рахував та виводив час їх виконання.
#
# Підсказка:
#
# from datetime import datetime
#
# now = datetime.now()

from datetime import datetime

numeric_01 = int(input("Прошу введіть перше число: "))
numeric_02 = int(input("Прошу введіть друге число: "))


def decorator(function_0):
    def wrapper(*args):
        now_time = datetime.now()
        result = function_0(*args)
        print(datetime.now() - now_time)
        return result
    return wrapper


@decorator
def function_01(a, b):
    return a + b


@decorator
def function_02(a, b):
    return a * b


# function_01 = function_01(numeric_01, numeric_02)
print(function_01(numeric_01, numeric_02))
print(function_02(numeric_01, numeric_02))
