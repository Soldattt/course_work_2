class Aircraft:
    """Класс получает объект класса GetApiAero, данные от пользователя о сортировке самолетов и выводит список"""


    __slots__ = ["callsign", "country", "velocity", "baro_altitude"]

    def __init__(self, callsign=None, country=None, velocity=None, baro_altitude=None):
        self.callsign = callsign
        self.country = country
        self.velocity = velocity
        self.baro_altitude = baro_altitude
        

    def __validate(self, data):
        """Метод для работы с информацией, получает информацию, сортирует по указанным пользователями параметрам
        и добавляет в список"""
        airplanes = data["states"][0]
        self.country = airplanes[2]
        self.callsign = airplanes[1]
        self.velocity = airplanes[9] if airplanes[8] == "False" else 0
        self.baro_altitude = airplanes[7] if airplanes[8] == "False" else 0


    def cast_to_object_list(self, aeroplanes):
        result = []
        for item in aeroplanes.get("states"):

            result.append(item)
        return result


    def __lt__(self, other: "Aircraft") -> bool:
        return self.baro_altitude < other.baro_altitude

    def __gt__(self, other: "Aircraft") -> bool:
        return self.baro_altitude > other.baro_altitude





