string1 = 'Съешь еще этих мягких французских булок ДА выпей же чаю'
print('Строка: ', string1)
print('4-е слово в строке в верхнем регистре: ', string1.split(" ")[3].upper())
print('7-е слово в строке в нижнем регистре: ', string1.split(" ")[6].lower())
print('3-я буква в 8-м слове: ', string1.split(" ")[7][2])
print('Каждое из слов в строке: ')
for i in range(len(string1.split(" "))):
    print(string1.split(" ")[i])
