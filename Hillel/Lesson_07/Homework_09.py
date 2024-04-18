import random

list_numeric_01 = [random.randint(1, 10) for i in range(1, 201)]
print(list_numeric_01)
dictionaly_01 = {key: list_numeric_01.count(key) for key in list_numeric_01}

print(dictionaly_01)
