import pytest
from automation_framework.utilities.api_helpers import ApiHelper
from automation_framework.utilities.db_helpers import DatabaseHelper

@pytest.fixture(scope="module")
def api():
    return ApiHelper()

@pytest.fixture(scope="module")
def db():
    return DatabaseHelper()

def test_get_weather_data(api,db):
    city = "Tbilisi"
    response = api.get_current_weather(city)
    json = response.json()
    db.insert_weather_data(city = city, temperature = json["main"]["temp"],feels_like = json["main"]["feels_like"])
    data = db.get_weather_data(city)
    assert data["temperature"] == json["main"]["temp"], "temperature does not match"
    assert data["feels_like"] == json["main"]["feels_like"], "feels_like does not match"
    assert response.status_code == 200, "response not 200"


def test_city_with_biggest_avg_temp(api,db):
    responses = api.get_city_weather_list()
    for response in responses:
        json = response.json()
        db.insert_weather_data(city = json['name'], temperature = json["main"]["temp"],feels_like = json["main"]["feels_like"])
        data = db.get_weather_data(json['name'])
        assert data["temperature"] == json["main"]["temp"], "temperature does not match"
        assert data["feels_like"] == json["main"]["feels_like"], "feels_like does not match"
        assert response.status_code == 200, "response not 200"






