anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}


def inner_join_shows(a, b):
    a_generes = []
    b_generes = []
    for key in a:
        a_generes.append(a[key])
    for key in b:
        b_generes.append(b[key])
    if len(set(a_generes) & set(b_generes)) > 0:
        return set(a_generes) & set(b_generes)
    else:
        return 'общих жанров нет'


print('Общие жанры Ани и Насти:', inner_join_shows(anya, nastya))
print('Общие жанры Оли и Светы:', inner_join_shows(olya, sveta))
print('Общие жанры Светы и Ани:', inner_join_shows(sveta, anya))
