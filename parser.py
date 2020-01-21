from bs4 import BeautifulSoup
from urllib.request import urlopen

html_stop = urlopen('https://yandex.ru/maps/213/moscow/stops/stop__9649856/?ll=37.533142%2C55.781578&z=17.68').read()
features = "html.parser"
Stoptime = BeautifulSoup(html_stop, features)
Bustime = Stoptime.find_all('li', 'masstransit-stop-panel-view__vehicle')
for bus in Bustime:
    namber = bus.find('a', 'link-wrapper masstransit-stop-panel-view__vehicle-name').text
    arrival = bus.find('span', 'masstransit-prognoses-view__title-text').text
    viewtime = bus.find('div', 'masstransit-prognoses-view__time').text
    print(arrival,'\n',viewtime)
