import allure
import pytest
import requests

from data import DataCourier, ResponseText
from urls import Urls, Endpoints


class TestCreateCourier:

    @allure.title('Создание нового курьера')
    def test_courier_registration_success(self, courier):

        courier_data = courier
        assert courier_data["status_code"] == 201 and courier_data["response_text"] == ResponseText.OK_TRUE

    @allure.title('Ошибка при создании двух одинаковых курьеров')
    def test_repeat_registration_failed(self, courier):

        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_courier}', data=courier["data"])

        assert response.status_code == 409 and ResponseText.ALREADY_USED in response.text

    @allure.title('Ошибка при создании курьера без заполнения обязательных полей')
    @pytest.mark.parametrize('courier_data', (DataCourier.invalid_data_without_login,
                                           DataCourier.invalid_data_without_password))
    def test_courier_registration_without_parameters_failed(self, courier_data):

        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_courier}', data=courier_data)

        assert response.status_code == 400 and ResponseText.NOT_ENOUGH_DATA_CREATE in response.text