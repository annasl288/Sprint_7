class Urls:
    SCOOTER_URL = "https://qa-scooter.praktikum-services.ru"


class Endpoints:
    courier = "/api/v1/courier"  # Создание/удаление курьера
    courier_login = f'{courier}/login'  # Логин курьера в системе
    create_order = "/api/v1/orders"  # Создание заказа / Получение списка заказов