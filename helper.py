import json

import allure
from faker import Faker


class CourierData:

    @staticmethod
    @allure.step('Сгенерировать данные для создания курьера')
    def generate_courier_data():
        fake = Faker()
        courier_body = {
            "login": fake.user_name(),
            "password": fake.passport_number(),
            "firstName": fake.first_name()
        }
        return courier_body

    @staticmethod
    @allure.step('Изменить данные для авторизации курьера')
    def change_courier_data_for_login(courier):
        courier.pop("firstName")
        courier_data_for_login = courier
        return courier_data_for_login

    @staticmethod
    @allure.step('Удалить поле из json')
    def delete_field_from_json(body, field):
        body.pop(field)
        body_changed = body
        return body_changed

    @staticmethod
    @allure.step('Сгенерировать данные для создания заказа')
    def generate_order_data(color):
        fake = Faker()
        body = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": fake.phone_number(),
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                    color
                     ]
        }
        order_body = json.dumps(body)
        return order_body


