#Вспомогательные функции для тестов

import requests
import random
import string
from api_methods.courier_methods import CourierMethods
from url import URL

#Функция генерирует случайную строку из букв нижнего регистра
def generate_random_string(length=10): 
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


#Функция генерирует рандомные данные курьера
def generate_courier_data():

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return {
        "login": login,
        "password": password,
        "first_name": first_name
    }


#Функция генерирует данные курьера без логина
def generate_courier_data_without_login():
    login = ""
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return {
        "login": login,
        "password": password,
        "first_name": first_name
    }


#Функция генерирует данные курьера без пароля
def generate_courier_data_without_password():
    login = generate_random_string(10)
    password = ""
    first_name = generate_random_string(10)
    return {
        "login": login,
        "password": password,
        "first_name": first_name
    }


#Функция регистрирует нового курьера и возвращает его данные
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
        URL.COURIER_ENDPOINT,
        data=payload
    )

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


#Получение ID курьера по логину и паролю
def get_courier_id(login, password):
    response = CourierMethods.login_courier(login, password)
    if response.status_code == 200:
        return response.json().get("id")
    return None


#Удаление курьера по ID
def delete_courier(courier_id):
    return CourierMethods.delete_courier(courier_id)