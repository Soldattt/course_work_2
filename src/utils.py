from heapq import nlargest


def filter_aeroplanes(data, filter_words):
    result = []
    if data:
        for i in data:
            for word in list(filter_words):

                if i["country"] == word:
                    result.append(i)

        return result


def get_aeroplanes_by_altitude(data, altitude_range):

    result = []
    if data:
        for i in data:
            if int(altitude_range[0]) <= i["baro_altitude"] <= int(altitude_range[1]):
                result.append(i)
        return result


def get_top_aeroplanes(data, top_n):
    if data:
        top = nlargest(top_n, data, key=lambda item: item["velocity"])
        if top:
            return top
        else:
            print("Самолетов по Вашему запросу не найдено")
    else:
        return "Самолетов по Вашему запросу не найдено"
