import allure
import pytest

from helper import CourierData
from functions.courier_api import CourierResponses
from constants import Messages


class TestCreateCourier:

    @allure.title('Создание курьера')
    @allure.description('Проверяем: курьера можно создать, запрос возвращает правильный код ответа, успешный запрос возвращает {"ok":true}')
    def test_create_courier(self, create_courier):
        courier_response = create_courier
        assert courier_response.status_code == 201 and courier_response.text == Messages.SUCCESS_CREATE

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_two_same_couriers(self):
        courier_body = CourierData.generate_courier_data()
        courier_response = CourierResponses.create_courier(courier_body)
        courier_v2_response = CourierResponses.create_courier(courier_body)
        delete_courier = CourierResponses.delete_courier(courier_body)

        assert courier_v2_response.status_code == 409 and courier_v2_response.json()[
            "message"] == Messages.DUPLICATE_COURIER

    # в документации указано сообщение "Этот логин уже используется",
    # но использую фактическое "Этот логин уже используется. Попробуйте другой."

    @allure.title('Нельзя создать курьера без заполнения обязательных полей')
    @pytest.mark.parametrize('field',
                             [
                                 pytest.param('login', id='test without login'),
                                 pytest.param('password', id='test without password')
                             ]
                             )
    def test_create_courier_without_required_fields(self, field):
        courier_body = CourierData.generate_courier_data()
        body_without_login = CourierData.delete_field_from_json(courier_body, field)
        courier_response = CourierResponses.create_courier(body_without_login)

        assert courier_response.status_code == 400 and courier_response.json()[
            "message"] == Messages.WITHOUT_REQUIRED_FIELD

    @allure.title('Нельзя создать курьера с существующим логином')
    def test_create_courier_with_existing_login(self):
        courier_body = CourierData.generate_courier_data()
        courier_v2_body = CourierData.generate_courier_data()
        courier_v2_body['login'] = courier_body['login']
        courier_response = CourierResponses.create_courier(courier_body)
        courier_v2_response = CourierResponses.create_courier(courier_v2_body)
        delete_courier = CourierResponses.delete_courier(courier_body)

        assert courier_v2_response.status_code == 409 and courier_v2_response.json()[
            "message"] == Messages.DUPLICATE_COURIER
