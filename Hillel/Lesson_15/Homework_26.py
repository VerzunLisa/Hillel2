# Створити програму-калькулятор у вигляді класу та кілька методів, як мінімум додавання, віднімання, ділення, множення, зведення в ступінь та вилучення квадратного кореня.
#
# Обернути кожен метод у блок try/except і зробити обробку кількох винятків, як мінімум ділення на 0.
#
# Створити свій виняток, наприклад, зведення в негативний ступінь.
class Calculator():
    def __init__(self, args_1, args_2):
        self.args_1 = args_1
        self.args_2 = args_2

    def talking_away(self, args_1, args_2):
        try:
            return args_1 - args_2
        except Exception:
            print('Перевірте вхідні данні, можливо там помилка')

    def plus(self, args_1, args_2):
        try:
            return args_1 + args_2
        except Exception:
            print('Перевірте вхідні данні, можливо там помилка')

    def multiplication(self, args_1, args_2):
        try:
            return args_1 * args_2
        except Exception:
            print('Перевірте вхідні данні, можливо там помилка')

    def division(self, args_1, args_2):
        try:
            return args_1 / args_2
        except ZeroDivisionError:
            print('Перевірте вхідні данні, у вас ділення на нуль')

    def raised_to_step(self, args_1, args_2):
        try:
            if args_2 > 0:
                return args_1 ** args_2
            else:
                raise NameError
        except NameError:
            print("Ви намагаєтесь привести, до ступіня від'ємне число")
        except Exception:
            print('Перевірте вхідні данні, можливо там помилка')

    def square_root(self, args_1):
        try:
            return args_1 ** 0.5
        except Exception:
            print('Перевірте вхідні данні, можливо там помилка')


a = Calculator(5, 0)
print(a.raised_to_step(2, 5))
