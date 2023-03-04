from unittest import TestCase

from task1 import geoids, statics, query

class TestStats(TestCase):
    def test_none(self):
        res = statics({})
        self.assertEqual(res, None)

    def test_two(self):
        res = statics({'facebook': 120, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98})
        self.assertEqual(res, 'facebook')

class TestGeoids(TestCase):
    def test_positive_number(self):
        res = geoids({'1': [268, 1, 2, 3, 45, 45, 8], '2': [268, 1 , 5, 6, 8], '3': [6, 8], '4': [0, 45, 55]})
        self.assertEqual(res, [0, 1, 2, 3, 5, 6, 8, 45, 55, 268])

    def test_negative_number(self):
        res = geoids({'1': [-268, 1, 2, -3, 45, 45, 8], '2': [268, -1, 5, 6, 8], '3': [6, -8], '4': [0, 45, 55]})
        self.assertEqual(res, [-268, -8, -3, -1, 0, 1, 2, 5, 6, 8, 45, 55, 268])

class TestQuery(TestCase):
    def test_none(self):
        res = query([])
        self.assertEqual(res, [])

    def test_str(self):
        res = query('hello world')
        self.failureException(res)

    def test_dict(self):
        res = query(['смотреть сериалы онлайн', 'новости спорта'])
        self.assertEqual(res, ['поисковых запросов из 3 слов - 50.0 %', 'поисковых запросов из 2 слов - 50.0 %']
)