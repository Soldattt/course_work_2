import os
from abc import ABC, abstractmethod

import requests
from dotenv import load_dotenv

load_dotenv()


URL_1 = os.getenv("URL_1")
URL_2 = os.getenv("URL_2")


class GetApi(ABC):
    """Абстрактный класс для получения данных из api"""

    @abstractmethod
    def get_api(self, *args, **kwargs):
        pass


class GetApiAero(GetApi):
    """Класс получает наименование страны, делает запросы о самолетах в этой стране и выводит список"""

    def __init__(self, country) -> None:
        """Метод конструктор"""
        self.openstreetmap_url = URL_1
        self.opensky_url = URL_2
        self.aeroplanes = None
        self.country = country

    def get_api(self):
        """Метод для работы с api, получает наименование страны,
        делает запросы о самолетах в этой стране и выводит список"""

        headers_nominatim = {
            "User-Agent": "test-app",
        }

        params_nominatim = {
            "country": self.country,
            "format": "json",
            "limit": 1,
        }

        response = requests.get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        data = response.json()

        geo_coordinates = data[0].get("boundingbox")

        params = {
            "lamin": geo_coordinates[0],
            "lamax": geo_coordinates[1],
            "lomin": geo_coordinates[2],
            "lomax": geo_coordinates[3],
        }

        response = requests.get(url=self.opensky_url, params=params)

        self.aeroplanes = response.json()

        return self.aeroplanes
