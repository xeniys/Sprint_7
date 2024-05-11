import pytest
import requests
from constants import Urls
from helper import CourierData
from functions.courier_api import CourierResponses


@pytest.fixture
def create_courier():
    courier_body = CourierData.generate_courier_data()
    courier = requests.post(Urls.BASE + Urls.CREATE_COURIER, courier_body)
    yield courier
    CourierResponses.delete_courier(courier_body)




