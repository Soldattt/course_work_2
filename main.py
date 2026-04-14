from src.aircraft import aircraft_list_from_opensky
from src.get_api import GetApiAero
from src.saver_info import InfoJSON
from src.utils import filter_aeroplanes, filter_by_altitude_range, format_aircraft_report, top_by_altitude


def user_interaction() -> None:
    country = input("Введите название страны (латиницей, например Belarus): ").strip()
    top_n = int(input("Введите количество самолётов для топа N: ").strip())
    if top_n <= 0:
        raise ValueError("N должно быть больше нуля")

    raw_filters = input("Страны регистрации через запятую (латиницей, например United States,Germany): ")
    filter_words = [w.strip() for w in raw_filters.split(",") if w.strip()]

    alt_raw = input("Диапазон высот через дефис, например 8000-12000: ").strip()
    low_s, high_s = [x.strip() for x in alt_raw.split("-", maxsplit=1)]
    altitude_low = float(low_s)
    altitude_high = float(high_s)

    api = GetApiAero(country)
    payload = api.get_api_opensky()
    if not payload:
        print("Не удалось получить данные о самолётах.")
        return

    planes = aircraft_list_from_opensky(payload)
    planes = filter_aeroplanes(planes, filter_words)
    planes = filter_by_altitude_range(planes, altitude_low, altitude_high)
    top_planes = top_by_altitude(planes, top_n)

    report = format_aircraft_report(top_planes)
    print(report)

    records = [p.cast_to_object_list() for p in top_planes]
    saver = InfoJSON()
    saver.add_info(records)


if __name__ == "__main__":
    user_interaction()
