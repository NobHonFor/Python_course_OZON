shows = {
    'Секретные материалы': 'фантастика',
    'Ведьмак': 'фэнтази',
    'Клан Сопрано': 'криминал',
    '24': 'драма',
    'Черное зеркало': 'фантастика',
    'Во все тяжкие': 'криминал',
    'Игра престолов': 'фэнтази',
    'Карточный домик': 'драма',
    'Рик и Морти': 'фантастика'
}
print('Жанр серриала Ведьмак: ', shows['Ведьмак'])
print()
print('Все сериаллы в списке: ')
for key in shows.keys():
    print(key)
print()
print('Все жанры в списке: ')
for values in shows.values():
    print(values)