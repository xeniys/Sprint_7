import pytest
import requests
from constants import Urls
from helper import CourierData


@pytest.fixture
def create_courier():
    courier_body = CourierData.generate_courier_data()
    courier = requests.post(Urls.BASE + Urls.CREATE_COURIER, courier_body)
    yield courier
    courier_login_data = CourierData.change_courier_data_for_login(courier_body)
    login_courier = requests.post(Urls.BASE + Urls.LOGIN_COURIER, courier_login_data)
    courier_id = str(login_courier.json()['id'])
    courier = requests.delete(Urls.BASE + Urls.DELETE_COURIER + courier_id)



