import allure
import requests
from data_test.constants import Constants
from data_test.user_data import DataForTest


class TestUpdateDataUser:

    @allure.title('Проверка возможности обновления даных юзера с валидным токеном')
    def test_updated_data_profile(self, prepare_token):
        headers = {'Authorization': prepare_token}
        response = requests.patch(Constants.URL + Constants.END_POINT_UPDATE_USER, headers=headers, data=DataForTest.updated_profile)
        assert response.status_code == 200 and response.json()['user']['name'] == 'sapunkova'

    @allure.title('Проверка возможности изменить данные юзера без авторизации')
    def test_create_user_fail(self):
        response = requests.patch(Constants.URL + Constants.END_POINT_UPDATE_USER, headers={'Authorization': ''}, data=DataForTest.data_double)
        assert response.status_code == 401
        assert "You should be authorised" in response.text







