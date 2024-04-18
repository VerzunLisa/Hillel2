numeric = input("Прошу ввести ціле додатне число: ")
if not numeric.isdigit() or int(numeric) <= 0:
    print("Ви ввели не вірні дані!")
else:
    numeric_01 = 0
    for numeric_02 in range(1, int(numeric)+1):
        if numeric_02 % 3 != 0:
            numeric_02 = numeric_02 ** 3
            numeric_01 += numeric_02
    else:
        print(numeric_01)
