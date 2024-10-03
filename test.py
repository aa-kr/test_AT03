
import pytest
from main import get_random_cat_image


def test_get_random_cat_image_success(mocker):
    # Мокируем метод requests.get
    mock_get = mocker.patch('main.requests.get')

    # Настраиваем мок для возврата успешного ответа
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"url": "https://cdn2.thecatapi.com/images/a2r.jpg"}
    ]

    # Вызываем функцию
    url = get_random_cat_image()

    # Проверяем, что возвращенный URL соответствует нашему мок-ответу
    assert url == "https://cdn2.thecatapi.com/images/a2r.jpg"

def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('main.requests.get')

    # Создаем мок-ответ для неуспешного запроса
    mock_get.return_value.status_code = 404

    url = get_random_cat_image()

    assert url is None

