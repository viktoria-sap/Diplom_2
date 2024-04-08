import allure
import pytest
import json
import requests
from data_test.constants import Constants
from data_test.user_data import DataForTest


class TestUpdateDataUser:
    @allure.step("Получаем авторизационный токен и записываем его в переменную")
    def get_token(self):
        token = requests.post(Constants.URL + Constants.END_POINT_LOGIN_USER, headers=Constants.headers, data=json.dumps(DataForTest.data_user))
        new_token = token.json()['accessToken']
        return new_token

    @allure.title('Проверка возможности обновления даных юзера с валидным токеном')
    @allure.step("Получаем токен и отправляем данные для изменения Имени")
    def test_updated_data_profile(self):
        new_token = self.get_token()
        response = requests.patch(Constants.URL + Constants.END_POINT_UPDATE_USER, headers={'Authorization': new_token}, data=DataForTest.updated_profile)
        assert response.status_code == 200 and response.json()['user']['name'] == 'sapunkova'

    @allure.title('Проверка возможности изменить данные юзера без авторизации')
    @allure.step("Отправка PATCH запроса - с измененными данными без авторизации")
    @pytest.mark.parametrize(("data", "status_code"), [(pytest.param(DataForTest.data_double, 400))])
    def test_create_user_fail(self, data, status_code):
        response = requests.patch(Constants.URL + Constants.END_POINT_UPDATE_USER, headers=Constants.headers, data=DataForTest.data_double, json=data)
        assert response.status_code == status_code
