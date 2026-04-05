
import pytest

from api_methods.courier_methods import CourierMethods
from helpers import (
    get_courier_id,
    delete_courier
)

#Фикстура только для очистки БД после теста. Не создает курьера, только удаляет.
@pytest.fixture(scope="function")
def cleanup_courier():
    courier_id = None
    #Функция для регистрации курьера, который будет удален после теста.
    def register_courier_for_cleanup(login, password):
        nonlocal courier_id
        courier_id = get_courier_id(login, password)
    
    yield register_courier_for_cleanup
    
    #Удаление курьера (выполнится даже при падении теста)
    if courier_id:
        delete_courier(courier_id)


