import time
import googlemaps
import os
from pathlib import Path


v_addr = 'Krowoderska 6'


class Trip:

    def __init__(self, addr):
        key = open(os.path.join(Path(__file__).parents[3], '.KEY'), 'r').read()
        self.gmaps = googlemaps.Client(key)
        stay_info = self.gmaps.geocode(addr)
        self.stay_fm_addr = stay_info[0]['formatted_address']
        self.stay_coord = stay_info[0]['geometry']['location'].values()
        self.stay_city = stay_info[0]['address_components'][3]['long_name']

    def _get_place_id(self, query):
        result = self.gmaps.find_place(input=query, input_type='textquery')
        place_id = result['candidates'][0]['place_id']
        return place_id

    def _get_place_coord(self, place_id):
        result = self.gmaps.place(place_id)['result']['geometry']['location']
        location = tuple(result.values())
        return location

    def _get_pids(self, query):
        params = {'query': query,
                  'location': self._get_place_coord(self._get_place_id(self.stay_city)),
                  'radius': 10000}

        x = self.gmaps.places(**params)
        ids = [place['place_id'] for place in x['results']]

        next_page = x.get('next_page_token', None)

        while next_page:
            params['page_token'] = next_page
            time.sleep(2)
            x1 = self.gmaps.places(**params)
            _ids = [place['place_id'] for place in x1['results']]
            ids.extend(_ids)
            next_page = x1.get('next_page_token', None)

        return ids

    def show_place_info(self, place_id):
        result = self.gmaps.place(place_id)
        return result

    def parse_places(self, query = 'Irish Pub', r=4):
        query = f'{query} {self.stay_city}'
        total = 0
        added = 0
        fmt = '{:70s}, {:10}, {}'
        pids = self._get_pids(query)
        output = []

        for pid in pids:
            total += 1
            _, result, status = self.show_place_info(pid).values()

            name = result.get('name', None)
            rating = result.get('rating', 0)
            types = result.get('types', None)
            reviews = result.get('reviews', None)
            addr = result.get('formatted_address', 'None')

            if rating >= r:

                if reviews:
                    for review in reviews:
                        rate = review.get('rating', None)
                        text = review.get('text', None)
                        print(name, addr)
                        print('{}:  {}'.format(rate, text))
                print('\n')
        print(output)

    def __str__(self):
        return f'You stay at {self.stay_fm_addr}'


t = Trip(v_addr)
print(t.parse_places())