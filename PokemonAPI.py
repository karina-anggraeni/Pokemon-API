## Tugas 16 Desember - POKEMON
## JCAH Data Science
## Karina Anggraeni

import requests

def Pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(nama)
    output = requests.get(url).json()

    # Nama Pokemon
    print('Nama pokemon: {}'.format(nama.title()))

    # Stats
    print('HP: {}'.format(output['stats'][0]['base_stat']))
    print('Attack: {}'.format(output['stats'][1]['base_stat']))
    print('Defense: {}'.format(output['stats'][2]['base_stat']))
    print('Speed: {}'.format(output['stats'][5]['base_stat']))

    # Tipe Pokemon
    print('Type: {}'.format(output['types'][0]['type']['name'].capitalize()))

    # Image
    print('Image: {}'.format(output['sprites']['other']['official-artwork']['front_default']))

    # Ability
    print('Abilities: ')
    for i in range(len(output['abilities'])):
        print('- {}'.format(output['abilities'][i]['ability']['name'].capitalize()))

# List seluruh pokemon
count = 898
url = 'https://pokeapi.co/api/v2/pokemon-species?offset=0&limit={}'.format(count)
output = requests.get(url).json()

all_pokemon = [output['results'][i]['name'] for i in range(len(output['results']))]

nama = ''

while nama.isalpha() == False:
    nama = input('Masukkan nama pokemon: ')
    if nama in all_pokemon:
        print('-+' * 20)
        Pokemon()
        print('-+' * 20)
    else:
        print('Pokemon tersebut tidak terdaftar. Silahkan masukkan nama pokemon lain.\n')