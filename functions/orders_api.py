import json

import allure
import requests

from constants import Urls


class OrderResponses:

    @staticmethod
    @allure.step('Отправить запрос на создание заказа')
    def create_order(order_body):
        order = requests.post(Urls.BASE + Urls.CREATE_ORDER, order_body)
        return order

    @staticmethod
    @allure.step('Отправить запрос на получение списка заказов')
    def get_orders():
        list_orders = requests.get(Urls.BASE + Urls.CREATE_ORDER + Urls.PARAMS_FOR_GET_ORDER)
        return list_orders

