from heapq import nlargest

from src.get_api import GetApiAero


class Aircraft:
    """Класс получает объект класса GetApiAero, данные от пользователя о сортировке самолетов и выводит список"""

    data = GetApiAero

    def __init__(self, data, country_user, top_n):
        """Метод конструктор"""
        self.identifier = None
        self.data = data
        self.info_airplanes = None
        self.country = country_user
        self.top_n = top_n

    def info(self):
        """Метод для работы с информацией, получает информацию, сортирует по указанным пользователями параметрам
        и добавляет в список"""
        result = []
        airplanes = self.data.get_api().get("states")
        for i in airplanes:
            if i[2].lower() == self.country:
                aeroplane = {"callsign": i[1], "country": i[2], "velocity": i[9], "baro_altitude": i[7]}
                result.append(aeroplane)
        if result:
            top = nlargest(self.top_n, result, key=lambda item: item["velocity"])
            return top
        else:
            return "Самолеты отсутствуют"
