
import allure
from api_methods.order_methods import OrderMethods


class TestOrderList:

    @allure.title("Получение списка заказов")
    @allure.description("Проверка полученря списка заказа без courierId курьера")
    def test_get_order_list_success(self):
        response = OrderMethods.get_order_list()

        assert response.status_code == 200