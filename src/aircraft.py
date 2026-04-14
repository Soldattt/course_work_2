class Aircraft:
    """Класс получает объект класса GetApiAero, данные от пользователя о сортировке самолетов и выводит список"""

    __slots__ = ["callsign", "country", "velocity", "baro_altitude"]

    def __init__(self, callsign=None, country=None, velocity=None, baro_altitude=None):
        self.callsign = callsign
        self.country = country
        self.velocity = velocity
        self.baro_altitude = baro_altitude
        self.__validate()

    def __validate(self):
        """Метод для проверки данных наличия борта"""
        if self.velocity is not None and not isinstance(self.velocity, (int, float)):
            raise ValueError("velocity должна быть числом или None")
        if self.baro_altitude is not None and not isinstance(self.baro_altitude, (int, float)):
            raise ValueError("baro_altitude должна быть числом или None")

    @classmethod
    def from_opensky_state(cls, data):
        """Метод для сбора объекта из одного элемента массива states"""
        if data is None:
            return None
        try:
            callsign = str(data[1] or "").strip()
            country = str(data[2] or "").strip()
            baro_altitude = data[7]
            velocity = data[9]
        except (IndexError, TypeError):
            return None
        if not callsign:
            return None
        return cls(callsign, country, velocity, baro_altitude)

    def cast_to_object_list(self):
        """Метод для создания словаря для записи в файл"""
        one_airplane = {
            "callsign": self.callsign,
            "country": self.country,
            "velocity": self.velocity,
            "baro_altitude": self.baro_altitude,
        }

        return one_airplane

    def __lt__(self, other: "Aircraft") -> bool:
        return self.baro_altitude < other.baro_altitude

    def __gt__(self, other: "Aircraft") -> bool:
        return self.baro_altitude > other.baro_altitude


def aircraft_list_from_opensky(payload):
    """Метод для преобразования ответа OpenSky в список объектов Aircraft."""
    if not payload or payload.get("states") is None:
        return []
    result = []
    for row in payload["states"]:
        plane = Aircraft.from_opensky_state(row)
        if plane is not None:
            result.append(plane)
    return result
