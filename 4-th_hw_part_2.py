anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

a = len(list(set(anya) & set(olya)))
b = len(list(set(anya) & set(nastya)))
c = len(list(set(anya) & set(sveta)))

if a > b and a > c:
    print('У Ани с Олей больше всего любимых сериалов')
elif b > a and b > c:
    print('У Ани с Настей больше всего любимых сериалов')
else:
    print('У Ани со Светой больше всего любимых сериалов')


