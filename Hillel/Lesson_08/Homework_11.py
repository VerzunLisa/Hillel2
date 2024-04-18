values = [1, 2, '3', 'forth', 'end', 99, True, None]
values_02 = map(lambda x: str(x) if type(x) == int or type(x) == float else x, values)
print(list(values_02))
