import json
from abc import ABC, abstractmethod
import os




project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_json = os.path.join(project_root, "data", "info.json")


class FileInfo(ABC):
    """Абстрактный класс для записи информации в файл json"""

    @abstractmethod
    def __init__(self):
        pass


    @abstractmethod
    def add_info(self):
        pass

    @abstractmethod
    def delete_info(self):
        pass

class InfoJSON(FileInfo):
    """Класс получает объект класса Aircraft и путь к файлу и записывает данные в файл, а также выводит в консоль"""

    def __init__(self, data):
        """Метод конструктор"""
        self.__path = path_json
        self.data = data


    def add_info(self):
        """Метод получает данные из класса Aircraft и путь к файлу и записывает данные в файл,
               а также выводит в консоль"""
        items = self.data
        print(items)
        print("Данные записаны в файл info.json")
        with open(f"{self.__path}", "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False)


    def delete_info(self):
        with open(f"{self.__path}", "w", encoding="utf-8") as f:
            f.truncate(0)
        print("Данные удалены из файла info.json")
