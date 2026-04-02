import pytest
import allure

from api_methods.order_methods import OrderMethods
from data import SCOOTER_COLORS
from generators import generate_random_order_dict


class TestCreateOrder:

    @allure.title("Создание закза с рандомными данными и разными цветами самоката")
    @allure.description("Проверка создания закза с рандомными данными и разными цветами самоката")
    @pytest.mark.parametrize("color", SCOOTER_COLORS)
    def test_create_order_with_different_scooter_colors(self, color):
        with allure.step("Отправляем запрос на создание заказаз с рандомными данными и разными цветами самоката"):
            order_data = generate_random_order_dict(color)
            response = OrderMethods.create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)
