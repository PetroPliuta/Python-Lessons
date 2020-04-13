"""Модуль працює з API - https://api.covid19api.com/summary
отримує ключ ["Countries"]
дозволяє сортувати отримане значення, виводити на екран, записувати в файл
"""
import requests
import json
import os
from operator import itemgetter
import csv


def get_countries():
    """Функція бере результат з API - https://api.covid19api.com/summary
    повертає JSON ключ ["Countries"] отриманого об'єкта
    """
    result = ""
    r = requests.get('https://api.covid19api.com/summary', timeout=10)
    if r.status_code == requests.codes.ok:
        result = r.json()["Countries"]
    return result


def sort_countries(countries: dict, sort_by='TotalConfirmed'):
    """Функція сортує отриманий dict
    по вказаному ключу sort_by
    """
    return sorted(countries, key=itemgetter(sort_by), reverse=True)


def print_top_countries(countries: dict, top=50):
    """Функція виводить ключі: ("Country", "TotalConfirmed") 
    з перших top записів отриманого dict
    """
    ukr_place: int
    print("Top countries\n%-33s%15s" % ("Country", "TotalConfirmed"))
    for i in range(top):
        print('{:03d}{:.<30}{:.>15}'.format(
            (i+1), ". " + countries[i]["Country"], countries[i]["TotalConfirmed"]))
        if countries[i]["Country"] == "Ukraine":
            ukr_place = i+1
    try:
        ukr_place
    except:
        pass
    else:
        print("\nUkraine is on ", ukr_place, " place", sep='')


def write_json_to_file(countries: dict, filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result.txt')):
    """Функція записує отриманий dict в файл
    у форматі json
    """
    file = open(filename, 'w')
    json.dump(countries, file, indent=4)
    file.close()


def write_csv_to_file(countries: dict, filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result.csv')):
    with open(filename, "w", newline="") as file:
        columns = countries[0].keys()
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(countries)
