import requests
host = 'https://api.pokemonbattle.me'

response = requests.post(url=f'{host}/v2/pokemons',
                         json={
                             'name': 'Legend Sam ',
                             'photo': 'https://dolnikov.ru/pokemons/albums/155.png',                  
                             },
                             headers={'Content-Type': 'application/json',
                                     'trainer_token': 'xxx'}, timeout=5)


print(f'Message:{response.text}')
                                     
response = requests.put(url=f'{host}/v2/pokemons',
                         json={
                             'pokemon_id': '7224',
                             'name': 'Senjor Sam',
                             'photo': 'https://dolnikov.ru/pokemons/albums/165.png',                  
                             },
                             headers={'Content-Type': 'application/json',
                                     'trainer_token': 'xxx'}, timeout=5)


print(f'Message:{response.text}')           

response = requests.post(url=f'{host}/trainers/add_pokeball',
                         json={
                             'pokemon_id': '7224'                                      
                             },
                             headers={'Content-Type': 'application/json',
                                     'trainer_token': 'xxx'}, timeout=5)


print(f'Message:{response.text}')     
