# 1. Створити 2 змінні з однаковими даними (і однаковим типом) та з однаковими ідентифікаторами (не присвоюючи значення змінних один одному)
#
# a_1 = ...
#
# a_2 = ...
#
# a1 == a2
#
# True
#
# a1 is a2
#
# True
#
# 2. Створити 2 змінні з однаковими даними (і однаковим типом) та з різними ідентифікаторами
#
# b_1 = ...
#
# b_2 = ...
#
# b_1 == b_2
#
# True
#
# b_1 is b_2
#
# False
#
# Замість «...» необхідно вставити якісь данні, при цьому у першому завданні обоїм змінним треба присвоєти однакові данні, та в другому завданні інші, але теж однако ві дані.
#
# 3. *Додаткове необов'язкове завдання:
#
# Поміняти їх типи так, щоб у 1-х двох змінних стали різні ідентифікатори, але при цьому залишилися однакові дані (і однаковим типом), а у 2-х останніх стали однакові ідентифікатори та залишилися однакові дані.
#
# Досягти потрібного результату необхідно лише приведенням типів даних до потрібного.
#
# a_1 = type_1(a_1)
#
# a_2 = type_1(a_2)
#
# a1 == a2
#
# True
#
# a1 is a2
#
# False
#
# b_1 = type_2(b_1)
#
# b_2 = type_2(b_2)
#
# b1 == b2
#
# True
#
# b1 is b2
#
# True

# type_1 – один тип даних
#
# type_2 – інший тип даних
data_01 = 18
data_02 = 18

print(data_01 == data_02)
print(data_01 is data_02)

data_03 = [18, 24, 6]
data_04 = [18, 24, 6]
print(data_03 == data_04)
print(data_03 is data_04)
print("-"*100)
data_01 = {data_01}
data_02 = {data_02}
print(data_01 == data_02)
print(data_01 is data_02)
data_03 = bool(data_03)
data_04 = bool(data_04)
print(data_03 == data_04)
print(data_03 is data_04)
