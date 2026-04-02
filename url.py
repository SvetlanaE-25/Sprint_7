class URL:
    BASE_URL = "http://qa-scooter.praktikum-services.ru"

    #Эндпоинты для курьеров
    COURIER_ENDPOINT = f"{BASE_URL}/api/v1/courier"
    COURIER_LOGIN_ENDPOINT = f"{COURIER_ENDPOINT}/login"
    COURIER_DELETE_ENDPOINT = f"{COURIER_ENDPOINT}/{{courier_id}}"

    # Эндпоинты для заказов
    CREATE_ORDER_ENDPOINT = f"{BASE_URL}/api/v1/orders"
    ORDER_LIST_ENDPOINT = f"{BASE_URL}/api/v1/orders"
