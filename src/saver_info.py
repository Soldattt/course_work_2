import json
import os
from abc import ABC, abstractmethod

from src.aircraft import Aircraft

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(project_root, "data", "info.json")


class SaverInfo(ABC):
    """Абстрактный класс для записи информации в файл json"""

    @abstractmethod
    def __init__(self, path):
        pass

    @abstractmethod
    def save_info(self):
        pass


class SaverInfoAircraft(SaverInfo):
    """Класс получает объект класса Aircraft и путь к файлу и записывает данные в файл, а также выводит в консоль"""

    data = Aircraft

    def __init__(self, data):
        """Метод конструктор"""
        super().__init__(path)
        self.data = data
        self.path = path

    def save_info(self):
        """Метод получает данные из класса Aircraft и путь к файлу и записывает данные в файл,
        а также выводит в консоль"""
        items = self.data.info()
        print(items)
        print("Данные записаны в файл info.json")
        with open(f"{path}", "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False)
