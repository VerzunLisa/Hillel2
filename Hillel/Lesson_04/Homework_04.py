name = input("Добрий день! Назвіться: ")
age = input("Скільки Вам років? : ")

if age.isdigit() <= 0 or not int(age):
    print("Помилка, повторіть введення.")
elif int(age) < 10:
    print("Привіт, шкет " + name)
elif int(age) <= 18:
    print("Як справи " + name+"?")
elif int(age) < 100:
    print("Що бажаєте " + name+"?")
else:
    print(name+" ви брешете, у наш час стільки не живуть...")

answear = input("Бажаєте вийти? (Д/У): ").upper()
while answear == "Д":
    name = input("Добрий день! Назвіться: ")
    age = input("Скільки Вам років? : ")

    if age.isdigit() <= 0 or not int(age):
        print("Помилка, повторіть введення.")
    elif int(age) < 10:
        print("Привіт, шкет " + name)
    elif int(age) <= 18:
        print("Як справи " + name + "?")
    elif int(age) < 100:
        print("Що бажаєте " + name + "?")
    else:
        print(name + " ви брешете, у наш час стільки не живуть...")

    answear = input("Бажаєте вийти? (Д/У): ").upper()
