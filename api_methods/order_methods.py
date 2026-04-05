import requests
import allure
from url import URL


class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(order_data: dict):
        return requests.post(URL.CREATE_ORDER_ENDPOINT, json=order_data)
    
    @staticmethod
    @allure.step("Получение списка заказов")
    def get_order_list():
        return requests.get(URL.ORDER_LIST_ENDPOINT)