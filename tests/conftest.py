
import pytest
import requests
import random
import string
from api_methods.courier_methods import CourierMethods
from api_methods.order_methods import OrderMethods
from generators import generate_random_order_dict


#Фикстура генерирует случайную строку
def generate_random_string(length=10): 
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))



#Фикстура генерирует рандомные данные курьера
@pytest.fixture
def generate_courier_data():

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return {
        "login": login,
        "password": password,
        "first_name": first_name
    }


#Фикстура генерирует данные курьера без логина
@pytest.fixture
def generate_courier_data_without_login():
    login = ""
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return {
        "login": login,
        "password": password,
        "first_name": first_name
    }


#Фикстура генерирует данные курьера без пароля
@pytest.fixture
def generate_courier_data_without_password():
    login = generate_random_string(10)
    password = ""
    first_name = generate_random_string(10)
    return {
        "login": login,
        "password": password,
        "first_name": first_name
    }


#Фикстура регистрирует нового курьера и возвращает его данные
@pytest.fixture(scope="function")
def register_new_courier_and_return_login_password():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier',
        data=payload
    )

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

#Фикстура создает рандомные данные для заказа
@pytest.fixture(scope="function")
def create_random_order_data():
    order_body = generate_random_order_dict()

    yield order_body  