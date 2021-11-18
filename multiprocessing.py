from datetime import datetime
from os import makedirs
from os.path import exists
from pprint import pprint
from shutil import copyfileobj, rmtree
from urllib.parse import urljoin
from requests import get

    """
    Ways to solve
    -Threads
    -asyncio
    -concurrence.feautes
    -multprocess
    """

path = 'downloads'
base_url = 'https://pokeapi.co/api/v2/'

if exists (path):
    rmtree(path)
makedirs(path)

def download_file(name, url, *, path='downloads', type='png'):
    response_download = get (url, stream = True)
    with open(f'{path}/{name}.{type}', 'wb') as f:
        copyfileobj(response_download.raw, f)
    return f'{path}/{name}'

def get_sprite_url(url, sprite='front_default'):
    return get(url).json()['sprites'][sprite]


pokemons = get ( urljoin( base_url, 'pokemon/?limite=10')).json()['results']

images_url = {j['name']: get_sprite_url(j['url']) for j in pokemons}

files = [download_file(name,url) for name, url in images_url.items()]


pprint(files)