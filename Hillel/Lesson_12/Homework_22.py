# Створити 2 класу truck та car, які є спадкоємцями класу auto з попереднього домашнього завдання.
#
# Об'єкти класу truck мають додатковий обов'язковий атрибут max_load.
#
# Перевизначений метод move перед появою напису «move» виводить напис «attention»,
# його реалізацію зробити з допомогою оператора super.
#
# А також додатковий метод load. При його виклику відбувається пауза 1 сек. потім видається повідомлення «load»
# і знову пауза 1 сек.
#
# Об'єкти класу car мають додатковий обов'язковий атрибут max_speed та при виклик методу move,
# після появи напису «move» має з'явитися напис "max speed is <max_speed>".
# Замість <max_speed> має виводиться значення обов'язкового атрибуму max_speed.
# Створити по 2 об'єкти для кожного з класів truck та car, перевірити всі їх методи та атрибути.
#
# При цьому об'єкти Truck і Car при створенні можуть приймати такі самі аргументи,
# що об'єкти класу Auto (brand, mark, age - обов'язкові, а color і weight - не обов'язкові).

import time


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
        return "move"

    def stop(self):
        print("stop")

    def birthday(self):
        return print(self.age + 1)

class Truck(Auto):

    def __init__(self, max_load, brand, age, mark, weight=5000, color="rad"):
        super().__init__(brand, age, mark, weight, color)
        self.max_load = max_load
        super().move()
        print("attention move")

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):

    def __init__(self, max_speed, brand, age, mark, weight=5000, color="grey"):
        super().__init__( brand, age, mark, weight, color)
        self.max_speed = max_speed

    def move(self):
        print("max speed is " + str(self.max_speed))


car_01 = Car(100, "Toyota", 10, "AV")
car_01.move()
car_01.stop()
car_01.birthday()
print(car_01.__dict__)
car_02 = Car(150, "Mitsubishi", 3, "AMN")
car_02.move()
car_02.stop()
car_02.birthday()
print(car_02.__dict__)

truck_01 = Truck(70, "Ukraine", 3, "ANX")
truck_01.load()
print(truck_01.__dict__)
truck_02 = Truck(70, "Poland", 8, "ADK")
truck_02.load()
print(truck_02.__dict__)