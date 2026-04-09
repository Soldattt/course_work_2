from heapq import nlargest


def filter_aeroplanes(data, filter_words):
    result = []
    if data:
        print(data)
        for i in data:
            for word in list(filter_words):

                if i[2] == word:
                    result.append(i)

        return result



def get_top_aeroplanes(data, top_n):
    if data:
        top = nlargest(top_n, data)
        if top:
            return top
        else:
            print("Самолетов по Вашему запросу не найдено")
    else:
        return "Самолетов по Вашему запросу не найдено"
