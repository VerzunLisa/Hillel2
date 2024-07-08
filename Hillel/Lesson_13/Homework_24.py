# Створіть власний клас String на основі стандартного класу str.
#
# В ньому необхідно:
#
# • Розширити стандартний метод, відповідальний за додавання
#
# • Написати відсутній у класі str метод відповідальний за віднімання
#
# Принцип роботи в новому класі String: об'єкти типу String можна додавати як між собою,
# так і з будь-яким іншим типом, який може бути приведений до типу рядка.
# "Під капотом", обидва операнди приводиться до типу рядків та потім відбувається конкаткатенація.
# Результатом додавання буде новий об'єкт класу String. Приклади виконання:
class String (str):
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        y = str(self) + str(other)
        return String(y)

    def __sub__(self, other):
        if str(other) in str(self):
            y = str(self).replace(str(other),"", 1)
            return String(y)
        else:
            return String(str(self))

line_01 = String("kalulsh")
line_02 = line_01 - "l"
line_03 = line_01 + [1461, 17461, "red"]
print(line_02)
print(type(line_02))
print(line_03)
print(type(line_03))
