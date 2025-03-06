import requests

class CityApi:
    BASE_URL = "https://countriesnow.space/api/v0.1/countries/cities"

    def get_city_list(self, country):
        payload = {"country": country}
        response = requests.post(self.BASE_URL, json=payload)
        return response.json()['data']

