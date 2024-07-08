class Car:
    FUEL_TYPES = ['бензин', 'дизель', 'електрика', 'гібрид']
    COLORS = []
    NUMBER_OF_CARS = 0

    def colour(self):
        if self.color != filter(lambda color: self.color, Car.COLORS):
            Car.COLORS = self.color

    def __init__(self, model, year, fuel_type, color):
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type.is_valid_fuel_type()
        self.numbers = get_number_of_cars()

    @classmethod
    def get_number_of_cars(cls):
        cls.NUMBER_OF_CARS += 1


    @staticmethod
    def is_valid_fuel_type(FUEL_TYPES):
        for fuel_type in FUEL_TYPES:
            return str(fuel_type)
        else:
            return str(FUEL_TYPES[0])

    def colour(self):
        if self.color != filter(lambda color: self.color, Car.COLORS):
            Car.COLORS = self.color


car_1 = Car('Zaz', 1979, 'дизель', 'black')
car_2 = Car('BMW', 2000, 'бензин', 'red')
car_3 = Car('VOLVO', 2012, 'електрикаcccc', 'black')
car_4 = Car('Mersedes', 2012, 'гібрид', 'black')

# print('COLORS:', Car.get_used_colors())
print('NUMBER_OF_CARS:', Car.get_number_of_cars())

for item in (car_1, car_2, car_3, car_4):
    print('item:', item)
    print('numbers:', item.numbers)
