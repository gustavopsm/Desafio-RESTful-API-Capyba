import json
from .models import ItemPrivado

def povoar():
    f = open('static/musicas_repeat.JSON')
    data = json.load(f)
    data = data['items']

    for musica in data:
        musica = musica['track']
        album = musica['album']['name']
        duration = musica['duration_ms']
        explicit = musica['explicit']
        name = musica['name']
        print(album, duration, explicit, name)
        ItemPrivado.objects.create(name=name, album=album, explicit=explicit, duration=duration)