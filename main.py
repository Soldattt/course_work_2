from src.aircraft import Aircraft
from src.get_api import GetApiAero
from src.saver_info import InfoJSON
from src.utils import filter_aeroplanes, get_aeroplanes_by_altitude, get_top_aeroplanes


# Функция для взаимодействия с пользователем
def user_interaction():
    country = input("Введите название страны:Belarus ")
    top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    filter_words = input(
        "Введите названия стран для фильтрации по стране регистрации (введите наименование стран через запятую): "
    ).split(",")
    altitude_range = input(
        "Введите диапазон высот полета (введите начальную и конечную высоту полета через тире '-'): "
    ).split(
        "-"
    )  # Пример: 100000 - 150000

    api = GetApiAero(country)

    # Получение информации о самолетах с opensky-network.org
    aeroplanes = api.get_api_opensky()

    # Преобразование набора данных в список объектов
    aero = Aircraft(aeroplanes)
    aeroplanes = aero.cast_to_object_list()

    filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)

    ranged_aeroplanes = get_aeroplanes_by_altitude(filtered_aeroplanes, altitude_range)

    top_aeroplanes = get_top_aeroplanes(ranged_aeroplanes, top_n)

    # Сохранение информации в файл
    json_saver = InfoJSON(top_aeroplanes)
    json_saver.add_info()
    # Удаление информации из файла
    json_saver.delete_info()


if __name__ == "__main__":
    user_interaction()
