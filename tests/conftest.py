
import pytest


from helpers import (
    generate_courier_data,
    generate_courier_data_without_login,
    generate_courier_data_without_password,
    register_new_courier_and_return_login_password,
    get_courier_id,
    delete_courier
)

from generators import generate_random_order_dict


#Фикстура возвращает рандомные данные курьера
@pytest.fixture()
def random_courier_data():
    return generate_courier_data()


#Фикстура предоставляет данные курьера без логина
@pytest.fixture
def courier_data_without_login():
    return generate_courier_data_without_login()


#Фикстура предоставляет данные курьера без пароля
@pytest.fixture
def courier_data_without_password():
    return generate_courier_data_without_password()

#Фикстура регистрирует нового курьера и возвращает его данные
@pytest.fixture(scope="function")
def register_new_courier_and_return_data():
    #Создаем курьера
    courier_data = register_new_courier_and_return_login_password()
    login, password, first_name = courier_data
    #Получаем ID курьера
    courier_id = get_courier_id(login, password)
    yield courier_data

    #Удаление курьера
    if courier_id:
        delete_courier(courier_id)



#Фикстура создает рандомные данные для заказа
@pytest.fixture(scope="function")
def create_random_order_data():
    order_body = generate_random_order_dict()

    return order_body  