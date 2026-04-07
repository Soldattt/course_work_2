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
    def get_api_openstreetmap(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_api_opensky(self, *args, **kwargs):
        pass



class GetApiAero(GetApi):
    """Класс получает наименование страны, делает запросы о самолетах в этой стране и выводит список"""

    def __init__(self, country:str) -> None:
        """Метод конструктор"""
        self.__openstreetmap_url = URL_1
        self.__opensky_url = URL_2
        self.aeroplanes = None
        self.__country = country

    def __connect(self):
        """Приватный метод проверки подключения к URL, при отсутствии подключения
        выводит сообщение об отсутствии подключения"""
        try:
            response_openstreetmap = requests.get(self.__openstreetmap_url)
            response_openstreetmap.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Ошибка подключения:", e)
        try:
            response_opensky = requests.get(self.__opensky_url)
            response_opensky.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Ошибка подключения:", e)

    def get_api_openstreetmap(self) -> list[dict]:
        """Метод для работы с api, получает наименование страны,
        делает запросы о самолетах в этой стране и выводит список самолетов"""

        headers_nominatim = {
            "User-Agent": "test-app",
        }

        params_nominatim = {
            "country": self.__country,
            "format": "json",
            "limit": 1,
        }

        response = requests.get(url=self.__openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        data = response.json()
        if data:
            return data[0].get("boundingbox")
        else:
            print("Данных по Вашей стране нет")


    def get_api_opensky(self) -> list:
        """Метод для работы с api, получает данные из предыдущего метода,
        делает запросы о самолетах в этой стране и выводит список самолетов по конкретным
        параметрам, если на вход поступает пустой список, выводит сообщение об отсутствии самолетов"""

        geo_coordinates = self.get_api_openstreetmap()
        if geo_coordinates:
            params = {
                "lamin": geo_coordinates[0],
                "lamax": geo_coordinates[1],
                "lomin": geo_coordinates[2],
                "lomax": geo_coordinates[3],
            }

            response = requests.get(url=self.__opensky_url, params=params)

            self.aeroplanes = response.json()

            return self.aeroplanes
        else:
            print("Самолетов нет")
