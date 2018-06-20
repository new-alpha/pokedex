from django.shortcuts import render
import requests
import json

BASE_URL = 'http://pokeapi.co'
def query_pokeapi(resource_uri):
    url = '{0}{1}'.format(resource_uri)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None


def pokeview(request):

    if 'pokename' in request.GET:
        pokename = request.GET['pokename']

        pokemon_url = '/api/v1/pokemon/{}/'.format(pokename)
        pokemon = query_pokeapi(pokemon_url)

        if pokemon:
            sprite_uri = pokemon['sprites'][0]['resource_uri']
            description_uri = pokemon['descriptions'][0]['resource_uri']

            sprite = query_pokeapi(sprite_uri)
            description = query_pokeapi(description_uri)

            return render(request, 'pokeview.html', {
                'pokemon': pokemon['name'],
                'description': description['description'],
                'sprite':BASE_URL + sprite['image']
                })

        else:
            return render(request,'pokeview.html',{})        
