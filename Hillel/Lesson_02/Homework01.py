# Написати програму використовуючи функції input() та print().
# Програма вимагає ввести довільну строку.
# Потім необхідно створити 2 строкові змінні, перша з яких складається лише з парних символів введеної строки,
# а друга складається з введеної строки, написаної у зворотній послідовності, при цьому всі літери повинні бути написані
# у верхньому регістрі.
#
# Як результат вивести введену строку та дві нові строки, що вийшли, кожну з нового рядка.
a = "Добрий день! Як ся маєте?"
print(a)

answer_01 = input("Відповідь: ")
print(answer_01)
b = answer_01[1::2]
print(b)
c = answer_01.upper()[::-1]

print(c)
