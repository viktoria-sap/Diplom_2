import json

import pytest
import requests
from data_test.constants import Constants
from data_test.user_data import DataForTest

@pytest.fixture()
def user_data():
    user_data = DataForTest()
    return user_data

@pytest.fixture()
def prepare_token():
    response = requests.post(Constants.URL + Constants.END_POINT_LOGIN_USER, headers=Constants.headers, data=json.dumps(DataForTest.data_user))
    token = response.json()['accessToken']
    return token

