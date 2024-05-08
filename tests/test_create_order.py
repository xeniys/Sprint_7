import allure
import pytest

from functions.orders_api import OrderResponses
from helper import CourierData


class TestCreateOrder:
    @allure.title('Создание заказа')
    @allure.description('Проверяем: заказ успешно создается, тело ответа содержит track.')
    @pytest.mark.parametrize('color',
                             [
                                 pytest.param('BLACK', id='black color'),
                                 pytest.param('GREY', id='grey color'),
                                 pytest.param(['BLACK', 'GREY'], id='black&grey color'),
                                 pytest.param([], id='empty color'),
                             ]
                             )
    def test_create_order(self, color):
        order_body = CourierData.generate_order_data(color)
        order_response = OrderResponses.create_order(order_body)

        assert order_response.status_code == 201 and order_response.json()['track'] is not None

    @allure.title('Получение списка заказов')
    def test_get_orders(self):
        order_list = OrderResponses.get_orders()

        assert order_list.status_code == 200 and 'orders' in order_list.json()