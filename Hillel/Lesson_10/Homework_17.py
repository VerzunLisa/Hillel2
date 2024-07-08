# Ввести з клавіатури 4 рядки та зберегти їх у 4 різні змінні.
#
# Створити файл і записати в нього перші 2 рядки та закрити файл.
#
# Потім відкрити файл на редагування і дозаписати 2 рядки, що залишилися.
#
# У підсумку файл має бути 4 рядки, кожен з яких повинен починатися з нового рядка.

text_1 = "Добрий день! "
text_2 = "Як у Вас справи? "
text_3 = "В мене все добре "
text_4 = "А у Вас?"

with open('complited_text.txt', 'w', encoding='utf-8') as complited:
    complited.writelines(text_1)
    complited.write('\n')
    complited.writelines(text_2)
    complited.write('\n')
complited.close()

with open('complited_text.txt', 'a', encoding='utf-8') as complited_1:
    complited_1.writelines(text_3)
    complited_1.write('\n')
    complited_1.writelines(text_4)
complited_1.close()
