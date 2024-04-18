numeric = input("Прошу ввести ціле додатне число: ")
index_01 = 1
numeric_01 = 1
numeric_02 = 0
while index_01 <= int(numeric):
    if int(index_01) % 3 != 0:
        numeric_01 = index_01**3
        numeric_02 += numeric_01
    index_01 += 1
else:
    print(numeric_02)
