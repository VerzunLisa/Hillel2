numeric = input("Прошу ввести число: ")
(print("Ви ввели парне число") if int(numeric) % 2 == 0 else print("Ви ввели непарне число")) if numeric.isdigit() else print("Помилка вводу")
