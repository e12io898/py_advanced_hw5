from test1 import logger
from datetime import datetime
import requests

@logger
def super(hero_list: list):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response, buffer = requests.get(url), []
    for superhero in response.json():
        if superhero['name'] in hero_list:
            buffer.append([superhero["name"],
                           superhero['powerstats']['intelligence']])
    sort_buffer = sorted(buffer, key=lambda x: x[1], reverse=True)
    return sort_buffer[0][0]

if __name__ == '__main__':
    super(['Hulk', 'Captain America', 'Thanos'])
