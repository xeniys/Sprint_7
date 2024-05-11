import sys

import allure
import pytest

from helper import CourierData
from functions.courier_api import CourierResponses
from constants import Messages


class TestLoginCourier:

    @allure.title('Логин курьера: курьер может авторизоваться')
    @allure.description('Проверяем: курьер может авторизоваться, успешный запрос возвращает id')
    def test_login_courier(self):
        courier_body = CourierData.generate_courier_data()
        CourierResponses.create_courier(courier_body)
        login_courier = CourierResponses.login_courier(courier_body)
        CourierResponses.delete_courier_after_login(courier_body)

        assert login_courier.status_code == 200 and login_courier.json()['id'] is not None

    @allure.title('Нельзя авторизоваться без заполнения обязательных полей')
    def test_login_courier_without_login(self):
        courier_body = CourierData.generate_courier_data()
        courier_body_org = courier_body.copy()
        CourierResponses.create_courier(courier_body)
        courier_body.pop('login')
        login_courier = CourierResponses.login_courier(courier_body)
        CourierResponses.delete_courier(courier_body_org)

        assert login_courier.status_code == 400 and login_courier.json()[
            'message'] == Messages.LOGIN_WITHOUT_REQUIRED_FIELD

    @allure.title('Нельзя авторизоваться с неправильными полями')
    @pytest.mark.parametrize('field',
                             [
                                 pytest.param('login', id='test with incorrect login'),
                                 pytest.param('password', id='test with incorrect password')
                             ]
                             )
    def test_login_courier_with_incorrect_data(self, field):
        courier_body = CourierData.generate_courier_data()
        courier_body_org = courier_body.copy()
        CourierResponses.create_courier(courier_body)
        courier_body[field] = courier_body[field] + 'fake'
        login_courier = CourierResponses.login_courier(courier_body)
        CourierResponses.delete_courier(courier_body_org)

        assert login_courier.status_code == 404 and login_courier.json()[
            'message'] == Messages.LOGIN_WITH_INCORRECT_DATA

    @allure.title('Нельзя авторизоваться с несуществующим пользователем')
    def test_login_courier_with_not_existing_user(self):
        courier_body = CourierData.generate_courier_data()
        login_courier = CourierResponses.login_courier(courier_body)

        assert login_courier.status_code == 404 and login_courier.json()[
            'message'] == Messages.LOGIN_WITH_INCORRECT_DATA
