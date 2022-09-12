import json
from .models import Item

def povoar():
    f = open('static/musicas.JSON')
    data = json.load(f)
    data = data['items']

    for musica in data:
        musica = musica['track']
        album = musica['album']['name']
        duration = musica['duration_ms']
        explicit = musica['explicit']
        name = musica['name']
        print(album, duration, explicit, name)
        Item.objects.create(name=name, album=album, explicit=explicit, duration=duration)

