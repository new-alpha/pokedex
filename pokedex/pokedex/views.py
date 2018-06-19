from django.core import serializers
from django.http import HttpResponse
import requests
import json

BASE_URL = 'http://pokeapi.co'

def query_pokeapi(resource_uri):
    url = '{0}{1}'.format(BASE_URL, resource_uri)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    return None


def pokeview(request):

    if 'pokename' in request.GET:
                pokename = request.GET['pokename']

    pokemon_url = '/api/v1/pokemon/{0}/'.format(pokename)
    pokemon = query_pokeapi(pokemon_url)

    stats = pokemon.object.all()

    info = serializers.serialize('json', stats)

    return HttpResponse(info, content_type='application/json')
