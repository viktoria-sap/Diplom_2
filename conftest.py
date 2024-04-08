import pytest

from data_test.user_data import DataForTest

@pytest.fixture()
def user_data():
    user_data = DataForTest()
    return user_data

