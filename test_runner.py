import cianparser


CONFIG = {
    'deal_type': 'sale',
    'accommodation_type': 'flat',
    'location': 'Казань',
    'start_page': 1,
    'end_page': 1,
    'is_saving_csv': True,
    'is_latin': False,
    'is_express_mode': False,
    'is_by_homeowner': False,
}
ROOMS = 2
URL_PARTS = [
    'https://kazan.cian.ru/cat.php?deal_type=sale',
    'engine_version=2',
    'floornl=1',
    'house_material%5B0%5D=1',
    'house_material%5B1%5D=2',
    'house_material%5B2%5D=8',
    'is_first_floor=0',
    'min_house_year=2010',
    'mintarea=35',
    'object_type%5B0%5D=1',
    'offer_type=flat',
    'only_flat=1',
    'region=4777',  # Казань
    'repair%5B0%5D=2',
    'repair%5B1%5D=3',
    'repair%5B2%5D=4',
    'room2=1',
    'with_neighbors=0',
]
URL = ''

if __name__ == '__main__':
    URL = '&'.join(URL_PARTS)
    if URL:
        data = cianparser.parse_by_url(search_url=URL, **CONFIG)
    else:
        data = cianparser.parse_auto(rooms=ROOMS, **CONFIG)
