import requests
from ya_disk import YaUploader
from unittest import TestCase


class TestYaUploader(TestCase):
    def setUp(self) -> None:
        with open('TOKEN_YA.txt', 'r') as file_ya:
            token_ya = file_ya.read().strip()
        token = YaUploader(token_ya)
        self.func_folder = token.get_create_folder('555')
        self.func_dell = token.get_delete_folder('555')



    def test_create_folder(self):
        res = self.func_folder
        self.assertEqual(res.status_code, 201)


    def test_error_409(self):
        self.assertNotEqual(self.func_folder.status_code, 409)

    def test_all_error(self):
        list_erorr = [400, 401, 403, 404, 406, 413, 423, 429, 503, 507]
        for i in list_erorr:
            self.assertNotEqual(self.func_folder.status_code, i)


    def tearDown(self):
        self.dell = self.func_dell

