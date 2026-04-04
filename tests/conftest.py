
import pytest

from api_methods.courier_methods import CourierMethods
from helpers import (
    generate_courier_data,
    register_new_courier_and_return_login_password,
    get_courier_id,
    delete_courier
)

#Фикстура создает курьера, возвращает даннные и удаляет его после теста
@pytest.fixture(scope="function")
def register_new_courier_and_delete():
    # Генерируем данные
    courier_data = generate_courier_data()
    login = courier_data["login"]
    password = courier_data["password"]
    first_name = courier_data["first_name"]
    
    # Создаем курьера
    response = CourierMethods.create_courier(login, password, first_name)
    
    #Получаем ID курьера
    courier_id = None
    if response.status_code == 201:
        courier_id = get_courier_id(login, password)
    
    # Передаем данные в тест
    yield {
        "login": login,
        "password": password,
        "first_name": first_name,
        "response": response,
        "courier_id": courier_id
    }
    
    #Очистка БД - выполнится даже при падении теста
    if courier_id:
        delete_courier(courier_id)
    

#Фикстура регистрирует нового курьера и возвращает его данные
@pytest.fixture(scope="function")
def register_new_courier_and_return_data():
    #Создаем курьера
    login, password, first_name = register_new_courier_and_return_login_password()
    #Получаем ID курьера
    courier_id = get_courier_id(login, password)
    yield login, password, first_name

    #Удаление курьера
    if courier_id:
        delete_courier(courier_id)

