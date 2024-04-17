import allure
import requests
import pytest

from data_test.user_data import DataForTest
from data_test.constants import Constants


class TestCreateOrder:
    @allure.title('Создания заказа без авторизации с ингредиентами')
    @pytest.mark.parametrize(("data", "status_code"), [(pytest.param(DataForTest.data_ingridient, 200))])
    def test_create_order_without_login_with_ingridients(self, data, status_code):
        response = requests.post(Constants.URL + Constants.END_POINT_ORDER, headers=Constants.headers, json=data).json()
        assert (status_code == 200 and response['success'] == True and response['name'] == "Бессмертный флюоресцентный бургер")

    @allure.title('Создания заказа без авторизации без ингредиентов')
    @pytest.mark.parametrize("data", [(pytest.param(DataForTest.data_not_ingridient))])
    def test_create_order_without_login_without_ingridients(self, data):
        response = requests.post(Constants.URL + Constants.END_POINT_ORDER, headers=Constants.headers, json=data)
        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.title('Создания заказа без авторизации с неверным хешем ингредиентов')
    @pytest.mark.parametrize("data", [(pytest.param(DataForTest.data_bad_ingridient))])
    def test_create_order_without_login_with_incorrect_hash(self, data):
        response = requests.post(Constants.URL + Constants.END_POINT_ORDER, headers=Constants.headers, json=data)
        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"One or more ids provided are incorrect"}'
