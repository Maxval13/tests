"""
Задача №1 unit-tests
Из курса «Python: программирование на каждый день и сверхбыстрое прототипирование» нужно написать тесты
на любые 3 задания из Лекции 4. Необходимо использовать своё решение домашнего задания.
При написании тестов не забывайте использовать параметризацию.
Рекомендации по тестам.
Если у вас в функциях информация выводилась(print), то теперь её лучше возвращать(return)
чтобы можно было протестировать.
"""

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def statics(stats):

    max_st = 0
    max_id = None
    for j, i in stats.items():
        if i > max_st:
            max_st = i
            max_id = j
    return max_id

queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт',
        ]

def query(queries):
    queries_dict = {}
    query_list = []
    j = 1
    for i in queries:
        if len(i.split()) not in queries_dict:
            queries_dict.setdefault(len(i.split()), j)
        else:
            queries_dict[len(i.split())] += 1
    for key, value in queries_dict.items():
        query_list.append(f'поисковых запросов из {key} слов - {round(((int(value)*100)/len(queries)),2)} %')
    return query_list

ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]}

def geoids(ids):
    geo_id = set()
    for ids_value in ids.values():
        for i in ids_value:
            geo_id.add(i)
    return sorted(list(geo_id))


print(statics(stats))
print(query(queries))
print(geoids(ids))
