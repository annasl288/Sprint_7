import allure
import pytest
import requests

from helpers import Courier
from data import DataCourier, ResponseText
from urls import Urls, Endpoints


class TestCourierLogin:

    @allure.title('Авторизация курьера с валидными данными')
    def test_courier_login_success(self, courier):

        courier_data = courier
        response = Courier().courier_login_and_get_id(courier_data["data"])

        assert response["status_code"] == 200 and response.get("id")

    @allure.title('Ошибка при авторизации курьера без заполнения обязательных полей')
    @pytest.mark.parametrize('courier_data', [DataCourier.invalid_data_without_login,
                                           DataCourier.invalid_data_without_password])
    def test_courier_login_without_parameters_failed(self, courier_data):

        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.courier_login}', data=courier_data)

        assert response.status_code == 400 and ResponseText.NOT_ENOUGH_DATA_LOGIN in response.text

    @allure.title('Ошибка при авторизации курьера с несуществующими данными')
    def test_courier_login_courier_does_not_exist_failed(self):

        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.courier_login}', data=DataCourier.invalid_data_courier_does_not_exist)

        assert response.status_code == 404 and ResponseText.ACCOUNT_NOT_FOUND in response.text
