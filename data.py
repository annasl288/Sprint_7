import datetime

from helpers import CreateCourierData


class DataCourier:
    # Валидные данные для регистрации
    valid_data = CreateCourierData.generate_valid_data_to_create_courier()

    # Невалидные данные для регистрации без поля "login"
    invalid_data_without_login = CreateCourierData.generate_invalid_data_to_create_courier_without_login()

    # Невалидные данные для регистрации без поля "password"
    invalid_data_without_password = CreateCourierData.generate_invalid_data_to_create_courier_without_password()

    # Данные несуществующего курьера
    invalid_data_courier_does_not_exist = {
        "login": "testLogin",
        "password": "testPassword"
    }


class DataOrder:
    # Данные для заказа самоката
    data = {
        "firstName": "Екатерина",
        "lastName": "Иванова",
        "address": "г.Москва",
        "metroStation": 2,
        "phone": "+79991234567",
        "rentTime": 4,
        "deliveryDate": f"{datetime.date.today()}",
        "comment": "Привезите поскорее!",
    }

class ResponseText:
    # Тексты ответов
    ALREADY_USED = "Этот логин уже используется"
    NOT_ENOUGH_DATA_CREATE = "Недостаточно данных для создания учетной записи"
    OK_TRUE = '{"ok":true}'
    NOT_ENOUGH_DATA_LOGIN = "Недостаточно данных для входа"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    TRACK = "track"

