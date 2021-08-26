birth_year = 0
cnt_year = 0
while True:
    try:
        birth_year = int(input('Введите год вашего рождения ?: '))
        break
    except ValueError:
        print('Для рассчета необходимо ввести год рождения')
        continue
while True:
    try:
        cnt_year = int(input('К какому году вы хотите рассчитать свой возраст?: '))
        break
    except ValueError:
        print('Для рассчета необходимо ввести год рождения')
        continue
print('К', cnt_year, 'году ваш возраст составит', (cnt_year - birth_year))
