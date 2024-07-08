# Створити генератор геометричної прогресії. При заданні початку прогресії -2 та кроку прогресії -5, генератор видає таку послідовність:
# -2
# 10
# -50
# 250
# -1250
# 6250
# ...
#
# При заданні початку прогресії 10 і кроку прогресії 3, генератор видає таку послідовність:
#
#  10
# 30
# 90
# 270
# 810
# 2430
# ...
def gener_1(x, y):
    while x < 6250:
        yield x
        x = x * y


for n in gener_1(-2, -5):
    print(n)
