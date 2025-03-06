import pytest
from selenium import webdriver
from automation_framework.utilities.city_api import CityApi
from automation_framework.utilities.api_helpers import ApiHelper
from automation_framework.utilities.weather_getter import *
import json

@pytest.fixture(scope="function")
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.timeanddate.com/weather/")
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def city_api():
    return CityApi()

@pytest.fixture(scope="module")
def api():
    return ApiHelper()


def test_time_and_date(driver, api, city_api):
    city_list = city_api.get_city_list("united kingdom")
    results = []
    for i in range(min(105, len(city_list))):
        city_name = city_list[i]

        try:
            temp_api = api.get_current_weather(city_name).json()["main"]["temp"]
            temp_ui = search_and_get_temp(driver=driver, city_name=city_name)

            temperature_diff = abs(temp_api - temp_ui)

            results.append({
                "city": city_name,
                "openweather_temp": temp_api,
                "timeanddate_temp": temp_ui,
                "temperature_diff": temperature_diff
            })
            print(i)

        except Exception as e:
            print(f"error processing city {city_name}: {e}")

    with open("temperature_report.json", "w") as f:
        json.dump(results, f, indent=4)
