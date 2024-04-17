import allure
import pytest
import requests

from data_test.user_data import DataForTest
from data_test.constants import Constants


class TestLoginUser:
    @allure.title('Проверка авторизации в системе с валидными данными')
    @pytest.mark.parametrize(("data", "status_code"), [(pytest.param(DataForTest.data_double, 200))])
    def test_login_user_correct(self, data, status_code):
        response = requests.post(Constants.URL + Constants.END_POINT_LOGIN_USER, headers=Constants.headers, json=data).json()
        assert response['success'] == True

    @allure.title('Проверка авторизации в системе с невалидными данными')
    @pytest.mark.parametrize(("data", "status_code"), [(pytest.param(DataForTest.data_login_fail, 400))])
    def test_login_user_fail(self, data, status_code):
        response = requests.post(Constants.URL + Constants.END_POINT_LOGIN_USER, headers=Constants.headers, json=data).json()
        assert response['message'] == "email or password are incorrect"

