import pytest
import requests


def test_user_info():
    '''
        Геоинформация о незарегистрированном пользователе доступна
    '''
    response = requests.get('https://user-geo-data.wildberries.ru/get-geo-info?currency=RUB&latitude=55.3662&longitude=86.0805&locale=ru&address=%D0%9A%D0%B5%D0%BC%D0%B5%D1%80%D0%BE%D0%B2%D0%BE&dt=0&currentLocale=ru&b2bMode=false')
    assert response.status_code == 200
    assert response.json()["address"] == "Кемерово"

def test_cart_info():
    '''
            Информация о содержимом корзины доступна
    '''
    response = requests.get('https://card.wb.ru/cards/v4/list?appType=1&curr=rub&dest=-1172839&spp=30&hide_dtype=13&ab_testing=false&lang=ru&nm=245750240;263573724;387832334;134332815;236250193;9391510;6216517&ignore_stocks=true')
    assert response.status_code == 200

def test_search_tickets_pos():
    '''
            Запрос на поиск авиабилетов отправляется успешно
    '''
    body = {
    "beginDate_at":"2025-07-13T00:00:00.000Z",
    "beginLocationCode":"MOW",
    "endLocationCode":"LED",
    "filter":{},
    "includeCorporateTariffs":False,
    "preferredAirlinesCodes":None,
    "promoUUID":None,
    "providers":["ot", "ac"],
    "seats": [{"passenger": "ADT", "number": 1}, {"passenger": "CHD", "number": 0}, {"passenger": "INF", "number": 0}],
    "serviceClass": "ECONOMY",
    "turnOnFolding": False
    }
    response = requests.post('https://travel.wildberries.ru/stream/api/avia-service/v1/stream/getFlights',json=body)
    assert response.status_code == 200


def test_search_tickets_neg():
    '''
            Запрос на поиск билетов без пассажиров выдает ошибку
    '''
    body = {
    "beginDate_at":"2025-07-13T00:00:00.000Z",
    "beginLocationCode":"MOW",
    "endLocationCode":"LED",
    "filter":{},
    "includeCorporateTariffs":False,
    "preferredAirlinesCodes":None,
    "promoUUID":None,
    "providers":["ot", "ac"],
    "seats": [{"passenger": "ADT", "number": 0}, {"passenger": "CHD", "number": 0}, {"passenger": "INF", "number": 0}],
    "serviceClass": "ECONOMY",
    "turnOnFolding": False
    }
    response = requests.post('https://travel.wildberries.ru/stream/api/avia-service/v1/stream/getFlights',json=body)
    assert response.status_code == 400


def test_unAuthorization():
    '''
            Просмотр информации о заказах пользователя недоступен без авторизации
    '''
    response = requests.get('https://wbxoofex.wildberries.ru/api/v2/orders')
    assert response.status_code == 401
