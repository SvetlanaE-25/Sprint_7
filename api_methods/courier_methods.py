import requests
import allure

from url import URL



class CourierMethods:

    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(login, password, first_name):
        payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
        return requests.post(URL.COURIER_ENDPOINT, data=payload)
    

    @staticmethod
    @allure.step("Логин курьера в системе") 
    def login_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(URL.COURIER_LOGIN_ENDPOINT, data=payload)
    
    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(URL.COURIER_DELETE_ENDPOINT.format(courier_id=courier_id))
    
    @staticmethod
    @allure.step("Получить id курьера")
    def get_courier_id(login, password):
        response = CourierMethods.login_courier(login, password)
        if response.status_code == 200:
            return response.json().get("id")
        return None