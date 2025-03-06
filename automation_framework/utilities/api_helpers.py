import requests
from automation_framework.utilities.config_reader import *
class ApiHelper:
    BASE_URL = config['DEFAULT']['BASE_URL']
    API_KEY = config['DEFAULT']['API_KEY']
    CITY_IDS = [11263, 14177, 18093, 3516149, 3516168, 3516188]

    def get_current_weather(self, city):
        url = f"{self.BASE_URL}?q={city}&appid={self.API_KEY}&units=metric"
        print(url)
        response = requests.get(url)
        print(response)
        return response


    def get_city_weather_list(self):
        responses = []
        for id in self.CITY_IDS:
            responses.append(requests.get(f"{self.BASE_URL}?id={id}&appid={self.API_KEY}"))
        return responses
