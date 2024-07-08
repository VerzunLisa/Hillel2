import pandas as pd
from datetime import datetime


def opening():
    return pd.read_excel('Data_basic.xlsx')


def save(new_data):
    return new_data.to_excel(r'C:\Users\Елизавета\PycharmProjects\Hillel2\Hillel\Diplom\Data_basic.xlsx', index=False)


def write_date():
    # with pd.ExcelWriter('Data_basic.xlsx') as writer:
        date_basic = pd.read_excel('Data_basic.xlsx')
        firstname = input("Вкажіть ім'я: ")
        lastname = input("Вкажіть прізвище: ")
        surname = input("Вкажіть по-батькові: ")
        date_of_people = input("Вкажіть дату народження: ").replace(".", '-', 2).replace("/", '-', 2).replace(" ", '-', 2)
        date_of_people = datetime.strptime(date_of_people, '%d-%m-%Y')
        date_of_death = input("Вкажіть дату смерті: ").replace(".", '-', 2).replace("/", '-', 2).replace(" ", '-', 2)
        if date_of_death == (False or None):
            date_of_death = datetime.today().strptime(date_of_death, '%d-%m-%Y')
        else:
            date_of_death = datetime.strptime(date_of_death, '%d-%m-%Y')
        become = input("Вкажіть стать: ")
        date_basic.loc[len(date_basic)+2] = [firstname, lastname, surname, date_of_people, date_of_death, become]
        # data = pd.DataFrame[firstname, lastname, surname, date_of_people, date_of_death, become]
        # df_marks = pd.concat([date_basic, data], ignore_index=True)
        return date_basic.to_excel('Data_basic.xlsx', index=False)

def search():
    date_basic = pd.read_excel('Data_basic.xlsx')
    search_date = input("Кого шукаєте?: ")
    for row_index, row in enumerate(date_basic):
        for col_index, col in enumerate(row):
            if col == search_date:
                return date_basic.iloc(col_index)
            break
        break
    else:
        "Нема співпадінь"



date_basic = search()
print(date_basic)
# writing_new = write_date()
