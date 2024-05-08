import allure
import requests

from constants import Urls
from helper import CourierData


class CourierResponses:
    @staticmethod
    @allure.step('Отправить запрос на создание курьера')
    def create_courier(courier_body):
        courier = requests.post(Urls.BASE + Urls.CREATE_COURIER, courier_body)
        return courier

    @staticmethod
    @allure.step('Отправить запрос на авторизацию курьера')
    def login_courier(courier_body):
        courier_login_data = CourierData.change_courier_data_for_login(courier_body)
        login_courier = requests.post(Urls.BASE + Urls.LOGIN_COURIER, courier_login_data)
        return login_courier

    @staticmethod
    @allure.step('Отправить запрос на удаление курьера')
    def delete_courier(courier_body):
        courier_login_data = CourierData.change_courier_data_for_login(courier_body)
        login_courier = requests.post(Urls.BASE + Urls.LOGIN_COURIER, courier_login_data)
        courier_id = str(login_courier.json()['id'])
        courier = requests.delete(Urls.BASE + Urls.DELETE_COURIER + courier_id)

    @staticmethod
    @allure.step('Отправить запрос на удаление курьера')
    def delete_courier_after_login(courier_body):
        login_courier = requests.post(Urls.BASE + Urls.LOGIN_COURIER, courier_body)
        courier_id = str(login_courier.json()['id'])
        courier = requests.delete(Urls.BASE + Urls.DELETE_COURIER + courier_id)



