# Створити батьківський клас auto, який має атрибути:
#
# brand, age, cоlor, mark і weight.
#
# А також методи: move, birthday і stop.
#
# Методи move і stop виводять повідомлення на екран «move» та «stop», а birthday збільшує атрибут age на 1.
#
# Атрибути brand, age та mark є обов'язковими під час оголошення об'єкта.

class Auto:
    brand = 'Honda'
    age = 10
    mark = "AJL"
    weight = None
    color = "blue"

    def __init__(self, brand, age, mark, weight=5000, color="yellow"):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.weight = weight
        self.color = color


    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self, age):
        return age + 1


auto_1 = Auto('Mitsubishi', 10,  "ASX")
print(auto_1.move())
