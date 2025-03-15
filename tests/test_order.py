import allure
import pytest
import requests
import json

from data import DataOrder, ResponseText
from urls import Urls, Endpoints


class TestOrder:

    @allure.title('Оформление заказа с разным набором цветов')
    @pytest.mark.parametrize('color', (
            {"color": ["BLACK"]},
            {"color": ["GREY"]},
            {"color": ["BLACK", "GRAY"]},
            {"color": [""]}
    ))
    def test_create_order_success(self, color):

        headers = {"Content-type": "application/json"}
        data = DataOrder.data
        data.update(color)
        data = json.dumps(data)
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.create_order}', headers=headers, data=data)

        assert response.status_code == 201 and ResponseText.TRACK in response.text

    @allure.title('Получение списка заказов')
    def test_get_orders_list_success(self):

        response = requests.get(f'{Urls.SCOOTER_URL}{Endpoints.get_orders_list}')

        assert response.status_code == 200 and len(response.content) > 0