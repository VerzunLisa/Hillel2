inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')
inputdata_02 = filter(lambda x: str(x[0:]).upper() == str(x[::-1]).upper(), inputdata)
print(list(inputdata_02))
