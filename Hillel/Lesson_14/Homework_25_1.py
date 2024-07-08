# Написати клас Car в якому є 3 атрибути класу:
#
# - FUEL_TYPES (список), в якому знаходиться перелік доступних значень
#
# типів авто, наприклад: ['бензин', 'дизель', 'електрика', 'гібрид']
#
# - COLORS (порожній список) – в якому зберігаються всі унікальні значення
#
# кольорів створених за цим класом об'єктів
#
# - NUMBER_OF_CARS - кількість створених об'єктів.
#
# Конструктор приймає 4 обов'язкові аргументи: model, year, color, fuel_type.
#
# Перші 3 аргументи присвоюються 3-м атрибутам об'єкта. В атрибут fuel_type
#
# об'єкту присвоюється результат статичного методу is_valid_fuel_type() в
#
# який передається аргумент fuel_type та атрибут класу FUEL_TYPES. Даний
#
# метод перевіряє, чи є значення fuel_type у списку FUEL_TYPES. Якщо
#
# входить, це значення повертається статичним методом is_valid_fuel_type(),
#
# якщо ні, то повертається перше значення списку FUEL_TYPES.
#
# Також у конструкторі необхідно збільшити атрибут класу NUMBER_OF_CARS на
#
# одиницю, а також внести до атрибуту класу COLORS аргумент color, якщо таке
#
# значення в атрибуті класу COLORS відсутнє. Крім цього у об'єкта повинен
#
# з'явиться атрибут number, до якого буде записано значення якой за рахунком
#
# цей об'єкт був створений (грубо кажучи значення NUMBER_OF_CARS на момент
#
# створення об'єкта).
#
# Також необхідно передбачити, щоб під час друку об'єкта роздруковувалося
#
# б: "модель – рік_випуску – тип_двигуна - колір" .
#
# У класу повинен бути метод numbers який би поводився як атрибут. При
#
# його виклику car.numbers має видаватися, наприклад: "2 from 4". Тобто
#
# це другий автомобіль із 4-х вироблених.
#
# Крім цього у класі повинні бути ще 2 методи класу get_used_colors() та
#
# get_number_of_cars(). Перший з яких повертає кількість унікальних
#
# кольорів вироблених автомобілів, грубо кажучи довжину списку COLORS.
#
# Другий метод повертає кількість всього вироблених автомобілів.
#
# class Car:
#
#     FUEL_TYPES = ['бензин', 'дизель', 'електрика', 'гібрид']
#
#     COLORS = []
#
#     NUMBER_OF_CARS = 0
#
# ...
#
# car_1 = Car('Zaz', 1979, 'дизель', 'black')
#
# car_2 = Car('BMW', 2000, 'бензин', 'red')
#
# car_3 = Car('VOLVO', 2012, 'електрикаcccc', 'black')
#
# car_4 = Car('Mersedes', 2012, 'гібрид', 'black')
#
# print('COLORS:', Car.get_used_colors())
#
# print('NUMBER_OF_CARS:', Car.get_number_of_cars())
#
# for item in (car_1, car_2, car_3, car_4):
#
#     print('item:', item)
#
#     print('numbers:', item.numbers)
class Car:
    FUEL_TYPES = ['бензин', 'дизель', 'електрика', 'гібрид']
    COLORS = []
    NUMBER_OF_CARS = 0

    def __init__(self, model, year,  color):
        self.model = model
        self.year = year
        self.color = color
        self.number = 0
        self.colors(color)
        self.get_number_of_cars()

        # self.fuel_type = fuel_type.is_valid_fuel_type(fuel_type)

    @staticmethod
    def is_valid_fuel_type():
        for fuel_type in Car.FUEL_TYPES:
            return fuel_type
        else:
            return Car.FUEL_TYPES[0]

    @classmethod
    def colors(cls, color):
        if not color in cls.COLORS:
            cls.COLORS.append(color)

    @classmethod
    def get_used_colors(cls):
        return len(cls.COLORS)

    @property
    def numbers(self):
        self.number += 1
        return f'{self.number} from {Car.NUMBER_OF_CARS}'

    @classmethod
    def get_number_of_cars(cls):
        return cls.NUMBER_OF_CARS


car_1 = Car('Zaz', 1979, 'black')
car_2 = Car('BMW', 2000, 'red')
car_3 = Car('VOLVO', 2012, 'black')
car_4 = Car('Mersedes', 2012, 'black')

print('COLORS:', Car.COLORS)
print('COLORS:', Car.get_used_colors())
print('NUMBER_OF_CARS:', Car.get_number_of_cars())

for item in (car_1, car_2, car_3, car_4):
    print('item:', item)
    print('numbers:', item.numbers)
