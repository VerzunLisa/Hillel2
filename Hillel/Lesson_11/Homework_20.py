# Прочитати збережений csv-файл із попереднього завдання та зберегти дані в excel-файл.
#
# Крім віку - стовпець з цими даними не потрібний.
#
# *Додаткове завдання не обов'язкове до виконання:
#
# розгорнути таблицю на дев'яносто градусів (стовпці стають рядками, а рядки стовпцями).
#
# До завдання прикріплений приклад як має виглядати змісту підсумкового файлу.

import csv
import pandas as pd

keys = ['ID', 'name', 'years', 'phone']
df1 = pd.DataFrame(keys)

with open('dictionare_tree.csv', 'r', encoding="utf-8") as file:
    read_book = csv.reader(file, delimiter=',')
    df2 = pd.DataFrame(read_book)
    df_consolide = pd.concat([df1, df2], axis=1)
    df_consolide_drop = df_consolide.drop(index=2)
    print(df_consolide_drop)
    df_consolide_drop.to_excel(r'C:\Users\Елизавета\PycharmProjects\Hillel2\Hillel\Lesson_11\test2.xlsx', index= False)
