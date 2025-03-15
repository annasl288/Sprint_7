import requests
from faker import Faker

from urls import Urls, Endpoints


class CreateCourierData:

    # Генерация валидных данных
    @staticmethod
    def generate_valid_data_to_create_courier():
        fake = Faker("ru_RU")

        login = fake.user_name()
        password = fake.password()
        first_name = fake.first_name()

        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return data

    # Генерация данных без поля "login"
    @staticmethod
    def generate_invalid_data_to_create_courier_without_login():
        fake = Faker("ru_RU")

        password = fake.password()
        first_name = fake.first_name()

        data = {
            "login": "",
            "password": password,
            "firstName": first_name
        }

        return data

    # Генерация данных без поля "password"
    @staticmethod
    def generate_invalid_data_to_create_courier_without_password():
        fake = Faker("ru_RU")

        login = fake.user_name()
        first_name = fake.first_name()

        data = {
            "login": login,
            "password": "",
            "firstName": first_name
        }

        return data


class Courier:

    # Регистрация в системе с возвратом кода ответа и данных курьера
    @staticmethod
    def create_new_courier_and_get_courier_data():
        data = CreateCourierData.generate_valid_data_to_create_courier()
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_courier}', data=data)
        return {"response_text": response.text, "status_code": response.status_code, "data": data}

    # Логин в системе с возвратом кода ответа и id курьера
    @staticmethod
    def courier_login_and_get_id(data):
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.courier_login}', data=data)
        return {"id": str(response.json()["id"]), "response_text": response.text, "status_code": response.status_code}