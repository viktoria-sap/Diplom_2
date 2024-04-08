from datetime import datetime


class DataForTest:
    data_200 = {
        "email": f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@yandex.ru',
        "password": "password",
        "name": "Username"
    }

    data_double = {
        "email": 'vickysap_vlgtest@gmail.com',
        "password": "12345678",
        "name": "vicky"
    }

    data_404 = {
        "email": f'test+{datetime.now().strftime("%m%d%Y%H%M%S")}@yandex.ru',
        "password": "password",
        "name": ""
    }

    data_login_fail = {
        "login": "",
        "password": ""
    }

    data_user = {
        "email": "vickysap_vlgtest1@gmail.com",
        "password": "123456789",
        "name": "vicky1"
    }

    updated_profile = {
        "email": "vickysap_vlgtest1@gmail.com",
        "password": "123456789",
        "name": "sapunkova"
    }

    data_ingridient = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

    data_not_ingridient = {
        "ingredients": []
    }

    data_bad_ingridient = {
        "ingredients": ["61c0c5a71d1f82001bdaaa61", "61c0c5a71d1f82001bdaaa61"]
    }