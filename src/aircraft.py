


class Aircraft:
    """Класс получает объект класса GetApiAero, данные от пользователя о сортировке самолетов и выводит список"""
    __slots__ = ["data", "country_check", "board_name", "speed", "altitude"]

    def __init__(self, data):
        """Метод конструктор"""
        self.data = data
        self.__validate()




    def __validate(self):
        """Метод для работы с информацией, получает информацию, сортирует по указанным пользователями параметрам
        и добавляет в список"""

        airplanes = self.data["states"][0]
        self.country_check = airplanes[2]
        self.board_name = airplanes[1]
        self.speed = airplanes[9] if airplanes[8] == "False" else 0
        self.altitude = airplanes[7] if airplanes[8] == "False" else 0


    def cast_to_object_list(self):
        result = []

        for airplane in self.data.get("states"):
            one_airplane = {"callsign": airplane[1], "country": airplane[2],
                     "velocity": airplane[9], "baro_altitude": airplane[7]}

            result.append(one_airplane)

        return result








