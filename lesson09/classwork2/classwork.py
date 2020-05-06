# import requests
from lib.db_manager import Db_manager
from lib.settings import HOST, USERNAME, PASSWORD

m = Db_manager(HOST, USERNAME, PASSWORD)
m.menu()

# covid19_data = requests.get(URL, timeout=10)
# print(covid19_data.json())
# r = requests.get('https://api.covid19api.com/summary', timeout=10)
