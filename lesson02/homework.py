#!/usr/bin/python3.8
import requests as req
# api.covid19api.com/summary


def sort_countries(countries: dict):
    sorted_ = {}
    for i in countries:
        sorted_[i["Country"]] = i["TotalConfirmed"]
    sorted_ = sorted(sorted_.items(), key=lambda x: x[1], reverse=True)
    return sorted_


r = req.get('https://api.covid19api.com/summary', timeout=10)
if r.status_code == req.codes.ok:
    result = r.json()
sorted_ = sort_countries(result["Countries"])

print("Top countries\n%-33s%15s" % ("Country", "TotalConfirmed"))
ukr_place: int
for i in range(100):
    print('{:03d}{:.<30}{:.>15}'.format(
        (i+1), ". " + sorted_[i][0], sorted_[i][1]))
    if sorted_[i][0] == "Ukraine":
        ukr_place = i+1
    # print("%-50s%20s" % (sorted_[i][0], sorted_[i][1]))

try:
    ukr_place
except:
    pass
else:
    print("\nUkraine is on ", ukr_place, "th place", sep='')
