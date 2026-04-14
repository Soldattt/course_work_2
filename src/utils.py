from heapq import nlargest

from src.aircraft import Aircraft


def filter_aeroplanes(data, filter_words):
    """Метод для сортировки бортов по выбранным странам."""
    words = {w.strip() for w in filter_words if w and w.strip()}
    if not words:
        return data
    return [p for p in data if p.country in words]


def filter_by_altitude_range(planes, altitude_low, altitude_high):
    """Метод для сортировки бортов по высоте."""
    out: list[Aircraft] = []
    for p in planes:
        if p.baro_altitude is None:
            continue
        if altitude_low <= float(p.baro_altitude) <= altitude_high:
            out.append(p)
    return out


def top_by_altitude(planes, top_n):
    """Метод для сравнения бортов по высоте через __lt__/__gt__ класса Aircraft."""
    if top_n <= 0:
        raise ValueError("top_n должен быть больше нуля")
    if not planes:
        return []
    return nlargest(top_n, planes)


def format_aircraft_report(planes):
    """Метод для вывода результата сортировки в консоль"""
    if not planes:
        return "Подходящих самолётов не найдено."
    lines: list[str] = []
    for i, p in enumerate(planes, start=1):
        cs = p.callsign or "—"
        alt = p.baro_altitude if p.baro_altitude is not None else "неизвестно"
        vel = p.velocity if p.velocity is not None else "неизвестно"
        lines.append(f"{i}. позывной: {cs}, страна: {p.country}, " f"высота: {alt}, скорость: {vel}")
    return "\n".join(lines)
