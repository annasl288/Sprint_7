import pytest

from helpers import Courier


# Регистрация и авторизация курьера
@pytest.fixture()
def courier():
    create_courier = Courier.create_new_courier_and_get_courier_data()
    courier_login = Courier.courier_login_and_get_id(create_courier["data"])
    yield create_courier
    Courier.courier_deletion(courier_login["id"])