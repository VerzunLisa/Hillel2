import random

name = input("Добрий день!. Як вас звуть?: ")
print("Вітаю " + name + "!\n Зараз я поясню вам правила гри. Сама гра називається Вгадай число.\n"
                        "Я загадаю число від 1 до 50. Ваша задача його вгадати.\n"
                        "На це у вас буде 5 спроб, я ж буду підказувати вам більше або меньше від "
                        "заданного вами числа.")
clue = input("Перед початком першої гри можу дати вам підказку. Хочете? (yes/ no): ").upper()
numeric = random.randint(1, 50,)
if clue == "YES":
    if numeric % 2 == 0:
        print("Число яке я загадала парне.")
    elif numeric % 2 != 0:
        print("Число яке я загадала непарне.")
elif clue == "NO":
    print("Ви відмовились від підказки. ")


def play(answear, numeric=numeric):
    if numeric > answear:
        print("Моє число більше за ваше")
    elif numeric < answear:
        print("Моє число меньше за ваше")


def tounament():
    attempt_start = 1
    attempt_finish = 5
    while attempt_start <= attempt_finish:
        answear_01 = int(input("Ваше число?: "))
        attempt_start += 1
        if answear_01 != numeric:
            play(answear_01)
        elif numeric == answear_01:
            print(" Мої вітання! Ви вгадали! Моє число " + str(answear_01))
            break


tounament()
new_gema = input("Хочете ще зіграти? (yes/no): ").upper()
while new_gema == "YES":
    tounament()
else:
    print("Щож на цьому завершуємо гру. До побачення!")