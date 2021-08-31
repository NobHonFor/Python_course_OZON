string1 = 'Съешь еще этих мягких французских булок ДА выпей же чаю'
work_str = string1.split(" ")
print('Строка: ', string1)
print('4-е слово в строке в верхнем регистре: ', work_str[3].upper())
print('7-е слово в строке в нижнем регистре: ', work_str[6].lower())
print('3-я буква в 8-м слове: ', work_str[7][2])
print('Каждое из слов в строке: ')
for i in range(len(work_str)):
    print(work_str[i])
