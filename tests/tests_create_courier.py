import allure

from api_methods.courier_methods import CourierMethods
from data import ERROR_MESSAGES
from helpers import (
    generate_courier_data_without_login,
    generate_courier_data_without_password,
    register_new_courier_and_return_login_password,
)

class TestCreateCourier:

    @allure.title("Создание курьера с рандомными данными")
    @allure.description("Проверка создания курьера с рандомными данными")
    def test_courier_create_success(self, register_new_courier_and_delete):
        with allure.step("Получаем ответ сервера после создания курьера"):
            response = register_new_courier_and_delete["response"]
        with allure.step("Проверяем ответ сервера"):
            assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
            assert response.json() == {"ok": True}
        #Очистка БД происходит автоматически в фикстуре register_new_courier_and_delete
    

    @allure.title("Cоздание дупликата курьера возвращает ошибку")
    @allure.description("Проверка создания курьера с повторяющимися данными")
    def test_duplicate_courier_create_error(self):
        with allure.step("Регистрируем нового курьера"):
            login, password, first_name = register_new_courier_and_return_login_password()
        
        with allure.step("Пытаемся создать курьера с теми же данными"):
            response = CourierMethods.create_courier(login, password, first_name)
        
        assert response.status_code == 409, f"Expected status code 409, but got {response.status_code}"
        assert response.json()["message"] == ERROR_MESSAGES["login_already_used"]
    
    @allure.title("Создание курьера без логина возвращает ошибку")
    @allure.description("Проверка создания курьера без логина")
    def test_create_courier_missing_login_error(self):
        with allure.step("Генерируем данные курьера без логина"):
            courier_data = generate_courier_data_without_login()
            login = courier_data["login"]
            password = courier_data["password"]
            first_name = courier_data["first_name"]
        
        with allure.step("Отправляем запрос на создание курьера с пустым полем логина"):
            response = CourierMethods.create_courier(login, password, first_name)
        
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        assert response.json()["message"] == ERROR_MESSAGES["missing_required_fields"]

    
    
    @allure.title("Создание курьера без пароля возвращает ошибку")
    @allure.description("Проверка создания курьера без пароля")
    def test_create_courier_missing_password_error(self):
        with allure.step("Генерируем данные курьера без пароля"):
            courier_data = generate_courier_data_without_password()
            login = courier_data["login"]
            password = courier_data["password"]
            first_name = courier_data["first_name"]
        
        with allure.step("Отправляем запрос на создание курьера с пустым полем пароля"):
            response = CourierMethods.create_courier(login, password, first_name)
        
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        assert response.json()["message"] == ERROR_MESSAGES["missing_required_fields"]