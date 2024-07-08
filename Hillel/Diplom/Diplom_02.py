import time

import pandas as pd
from datetime import datetime
from datetime import timedelta


def opening():
    return pd.read_excel('Data_basic.xlsx')


def write_date():
    date_of_life = ['ЖИВИЙ', 'ЖИВА', 'ЖИВ', 'НЕ ПОМЕР']
    date_basic = pd.read_excel('Data_basic.xlsx')
    firstname = input("Вкажіть ім'я: ")
    lastname = input("Вкажіть прізвище: ")
    surname = input("Вкажіть по-батькові: ")
    date_of_people = input("Вкажіть дату народження: ").replace(".", '-', 2).replace("/", '-', 2).replace(" ", '-', 2)
    date_of_people = datetime.strptime(date_of_people, '%d-%m-%Y')
    date_of_death = input("Вкажіть дату смерті: ")
    if date_of_death.upper() in date_of_life:
        # date_of_death = date_of_death.replace(".", '-', 2).replace("/", '-', 2).replace(" ", '-', 2)
        date_of_death = datetime.today()
    else:
        date_of_death = date_of_death.replace(".", '-', 2).replace("/", '-', 2).replace(" ", '-', 2)
        date_of_death = datetime.strptime(date_of_death, '%d-%m-%Y')
    years = (date_of_death - date_of_people)//year
    become = input("Вкажіть стать: ")
    date_basic.loc[len(date_basic)+2] = [firstname, lastname, surname, date_of_people, date_of_death,years, become]
    return date_basic.to_excel('Data_basic.xlsx', index=False)


def search():
    date_basic = pd.read_excel('Data_basic.xlsx')
    search_date = input("Кого шукаєте?: ").title()
    answear_date = date_basic[(date_basic['Імя'] == search_date) | (date_basic['Прізвище'] == search_date) | (date_basic['по батькові'] == search_date)|(date_basic['Імя'].str.contains(search_date)) |(date_basic['Прізвище'].str.contains(search_date)) |(date_basic['по батькові'].str.contains(search_date))]
    return print(answear_date)


def age_of_people(date_of_people, date_of_death):

    if date_of_people > date_of_death:
        print("У вас помилка в даті народження або даті смерті")
    else:
        age = date_of_death - date_of_people
    if int(age//year) == 1:
        return f'{int(age//year)} рік'
    elif (1 < int(age//year) > 11 or 19 < int(age//year)) and filter(lambda age: int(age[-1]), end_0):
        age = int(age//year)
        return f'{age} рік'
    elif (1 < int(age//year) > 11 or 19 < int(age//year)) and filter(lambda age: int(age[-1]), end_1):
        age = int(age // year)
        return f'{age} роки'
    elif (1 < int(age//year) > 11 or 19 < int(age//year)) and filter(lambda age: int(age[-1]), end_2):
        age = int(age // year)
        return f'{age} років'
    elif 10 < int(age//year) > 20:
        age = int(age // year)
        return f'{age} років'


year = timedelta(days=365)
mounts = timedelta(days=30)

end_0 = [1] # рік
end_1 = [2, 3, 4] # роки
end_2 = [5, 6, 7, 8, 9, 0] # років

add_to_table = ['ДОДАТИ ДАННІ', 'ДОДАТИ', 'ЗАПИС', 'ЗАПИСАТИ', 'ЗАПИСАТИ ДАННІ']
see_table = ['ПЕРЕГЛЯНУТИ', 'ПОДИВИТИСЬ', 'ПОДИВИТИСЬ ТАБЛИЦЮ', 'ПЕРЕГЛЯНУТИ ТАБЛИЦЮ']
search_in_table = ['ЗНАЙТИ', 'ПОШУК', 'ВІДНАЙТИ']

print("Добрий день. я можу допомогти розібратися з базою данних 'Data_basic.xlsx'")
time.sleep(3)

while True:
    answear_01 = input("Що Ви хочете зробити?\n - Переглянути таблицю?\n - Щось додати у таблицю?\n - Знайти когось в таблиці? :").upper()
    if answear_01 in see_table:
        print(opening())
        time.sleep(4)
    elif answear_01 in add_to_table:
        print(write_date())
        time.sleep(4)
    elif answear_01 in search_in_table:
        print(search())
        time.sleep(4)
    else:
        print("Не зрозуміла вашого запиту")
        time.sleep(4)
