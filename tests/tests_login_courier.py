
import allure
from api_methods.courier_methods import CourierMethods

class TestLoginCourier:

    @allure.title("Вход курьера с рандомными данными")
    @allure.description("Проверка входа курьера с рандомными данными")
    def test_courier_login_success(self, register_new_courier_and_return_login_password):
        login, password, _ = register_new_courier_and_return_login_password
        response = CourierMethods.login_courier(login, password)

        assert response.status_code == 200
        assert "id" in response.json()

    
    @allure.title("Вход курьера с неверными логином")
    @allure.description("Проверка ошибки при входе курьера с неверным логином")
    def test_login_wrong_login(self, register_new_courier_and_return_login_password):
        password = register_new_courier_and_return_login_password[1]
        
        response = CourierMethods.login_courier("wrong_login", password)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

        
    @allure.title("Вход курьера с неверными паролем")
    @allure.description("Проверка ошибки при входе курьера без с неверным паролем")
    def test_login_wrong_password(self, register_new_courier_and_return_login_password):
        login = register_new_courier_and_return_login_password[0]
        
        response = CourierMethods.login_courier(login, "wrong_password")
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"


    
    @allure.title("Вход курьера без логина")
    @allure.description("Проверка ошибки при входе курьера без логина")
    def test_login_missing_login(self, register_new_courier_and_return_login_password):

        password = register_new_courier_and_return_login_password[1]
        
        response = CourierMethods.login_courier("", password)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"


    @allure.title("Вход курьера без пароля")
    @allure.description("Проверка ошибки при входе курьера без пароля")
    def test_login_missing_password(self, register_new_courier_and_return_login_password):
        login = register_new_courier_and_return_login_password[0]
        
        response = CourierMethods.login_courier(login, "")
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    
    @allure.title("Авторизация несуществующего пользователя")
    @allure.description("Проверка ошибки при авторизации несуществующего пользователя")
    def test_login_nonexistent_user(self):
        response = CourierMethods.login_courier("nonexistent_user", "any_password")
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"