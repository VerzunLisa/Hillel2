variable_01, variable_02 = input("Прошу ввести речення з 2 слів: ").split()
print(variable_01+" "+variable_02, end="<<<>>>")
variable_01 = variable_01.capitalize()
variable_02 = variable_02.upper()

sentence_01 = "!%s %s?"
print(sentence_01 % (variable_02, variable_01), end="<<<>>>")
sentence_02 = "!{variable_02} {variable_01}?".format(variable_02=variable_02, variable_01=variable_01)
print(sentence_02, end="<<<>>>")
sentence_03 = f"!{variable_02} {variable_01}?"
print(sentence_03)
