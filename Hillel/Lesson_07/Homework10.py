# Написати лямбда-функцію визначальну парне/непарне.
#
# Функція приймає параметр (число) і якщо парне, видає слово “парне”, якщо ні - то “не парне”.
#
# *Додаткове не обов'язкове завдання:
#
# лямбда-функція вміє визначати як парне чи парне, а й число нуль.

x = int(input("Введіть число: "))

numeric = lambda x: "У вас парне число" if x % 2 == 0 else "У вас непарне число"
print(numeric(x))
