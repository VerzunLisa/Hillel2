x = int(input("Введіть число: "))

numeric = lambda x: "У вас парне число" if x % 2 == 0 else "У вас непарне число"
print(numeric(x))
