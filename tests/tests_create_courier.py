import allure

from api_methods.courier_methods import CourierMethods
from data import ERROR_MESSAGES


class TestCreateCourier:

    @allure.title("Создание курьера с рандомными данными")
    @allure.description("Проверка создания курьера с рандомными данными")
    def test_courier_create_success(self, random_courier_data):
        with allure.step("Отправляем запрос на создание курьера с рандомными данными"):
            login = random_courier_data["login"]
            password = random_courier_data["password"]
            first_name = random_courier_data["first_name"]
            response = CourierMethods.create_courier(login, password, first_name )
        
        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
        assert response.json() == {"ok": True}
        
    

    @allure.title("Cоздание дупликата курьера возвращает ошибку")
    @allure.description("Проверка создания курьера с повторяющимися данными")
    def test_duplicate_courier_create_error(self, register_new_courier_and_return_data):
        with allure.step("Отправляем запрос на создание курьера с данными зарегистрированного курьера"):
            login, password, first_name = register_new_courier_and_return_data
            response = CourierMethods.create_courier(login, password, first_name)
        
        assert response.status_code == 409, f"Expected status code 409, but got {response.status_code}"
        assert response.json()["message"] == ERROR_MESSAGES["login_already_used"]

    
    @allure.title("Создание курьера без логина возвращает ошибку")
    @allure.description("Проверка создания курьера без логина")
    def test_create_courier_missing_login_error(self, courier_data_without_login):
        with allure.step("Отправляем запрос на создание курьера с паролем, именем и пустым полем логина"):
            login = courier_data_without_login["login"]
            password = courier_data_without_login["password"]
            first_name = courier_data_without_login["first_name"]
            response = CourierMethods.create_courier(login, password, first_name )
        
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        assert response.json()["message"] == ERROR_MESSAGES["missing_required_fields"]

    
    
    @allure.title("Создание курьера без пароля возвращает ошибку")
    @allure.description("Проверка создания курьера без пароля")
    def test_create_courier_missing_password_error(self, courier_data_without_password):
        with allure.step("Отправляем запрос на создание курьера с логином, именем и пустым полем пароля"):
            login = courier_data_without_password["login"]
            password = courier_data_without_password["password"]
            first_name = courier_data_without_password["first_name"]            
            response = CourierMethods.create_courier(login, password, first_name)
        
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        assert response.json()["message"] == ERROR_MESSAGES["missing_required_fields"]