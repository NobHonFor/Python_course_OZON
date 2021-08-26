'''''
first_salary = float(input('Введите размер заработной платы: '))
second_salary = float(input('Введите размер заработной платы: '))
third_salary = float(input('Введите размер заработной платы: '))
avr_salary = float((first_salary + second_salary + third_salary)/3)
print('Средний доход составит: ', round(avr_salary, 3))
''''''
"""
first_salary = input()
second_salary = 0
third_salary = 0
if type(first_salary) == int or type(first_salary) == float:
    second_salary = input()
else:
    print('Для рассчета необходимо ввести число')
    exit()
if type(second_salary) == int or type(second_salary) == float:
    third_salary = input()
else:
    print('Для рассчета необходимо ввести число')
    exit()
if type(third_salary) == int or type(third_salary) == float:
    third_salary = input()
else:
    print('Для рассчета необходимо ввести число')
    exit()
print('Средний доход семьи составит:', (first_salary + second_salary + third_salary)/3)
"""
'''''
a = open(player_log.txt, 'w')