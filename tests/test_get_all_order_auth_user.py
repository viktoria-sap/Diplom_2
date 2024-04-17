import allure
import requests

from data_test.constants import Constants
from data_test.user_data import DataForTest


class TestGetOrderUser:

    @allure.title("Запрос на получение заказов авторизованного пользователя")
    def test_get_order_login_user(self, prepare_token):
        headers = {'Authorization': prepare_token}
        response = requests.get(Constants.URL + Constants.END_POINT_ORDER, headers=headers, data=DataForTest.updated_profile)
        body = response
        assert response.status_code == 200 and body.json()['success'] == True

    @allure.title("Запрос на получение заказов неавторизованного пользователя")
    def test_updated_order_not_login_user(self):
        response = requests.get(Constants.URL + Constants.END_POINT_ORDER, headers=Constants.headers)
        assert response.status_code == 401 and response.json()['success'] == False
