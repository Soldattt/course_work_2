from __future__ import annotations

import json
import os
from abc import ABC, abstractmethod
from typing import Any

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _default_json_path():
    return os.path.join(project_root, "data", "info.json")


def _default_csv_path():
    return os.path.join(project_root, "data", "info.csv")


class FileInfo(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def add_info(self, records: list[dict[str, Any]]) -> None:
        pass

    @abstractmethod
    def delete_info(self) -> None:
        pass


class InfoJSON(FileInfo):
    """Класс для работы с файлом"""

    def __init__(self, file_path: str | None = None) -> None:
        self.__path = file_path if file_path is not None else _default_json_path()

    def add_info(self, data):
        """Метод записи данных в файл"""
        items = data
        print("Данные записаны в файл info.json")
        with open(f"{self.__path}", "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False)

    def delete_info(self):
        """Метод очистки файла от данных"""
        os.makedirs(os.path.dirname(self.__path), exist_ok=True)
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False)
