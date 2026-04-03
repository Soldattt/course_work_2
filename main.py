from src.aircraft import Aircraft
from src.get_api import GetApiAero
from src.saver_info import SaverInfoAircraft


def user_interaction():
    """Функция запрашивает данные у пользователя и передает в модули для работы"""
    country = input("Введите название страны на латинице (например Belarus): ").lower()
    top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    country_user = input(
        "Введите названия страны для фильтрации по стране регистрации на латинице (например Poland): "
    ).lower()
    api = GetApiAero(country)
    api.get_api()
    air = Aircraft(api, country_user, top_n)
    air.info()
    result = SaverInfoAircraft(air)
    return result.save_info()


if __name__ == "__main__":
    user_interaction()
