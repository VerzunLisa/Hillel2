# Для класу Circle, розглянутому на уроці, додати метод віднімання двох кіл.
# У результаті віднімання двох кіл буде об'єкт класу Circle у которого будуть нові значення х, у та радіуса.
# Віднімання радіусов зробити по модулю. Якщо два кола з однаковим значенням радіуса віднімаються,
# то результатом віднімання буде об'єкт классу Point.

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{x}, y = {y}'

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.radius = radius

    def __str__(self):
        return f'x = {self.x}, y = {self.y}, radius = {self.radius}'

    def __sub__(self, other):
        if self.radius != other.radius:
            x = self.x - other.x
            y = self.y - other.y
            radius = abs(self.radius - other.radius)
            return Circle(x, y, radius)
        else:
            return super().__sub__().__str__()

circle_01 = Circle(5, 8, 4)
circle_02 = Circle(3, 8, 4)
circle_03 = circle_01 - circle_02
print(circle_03)
