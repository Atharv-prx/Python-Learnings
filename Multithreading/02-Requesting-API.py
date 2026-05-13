import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"

    try:
        response = requests.get(url, timeout = 5) # This method is gonna return a response object,   
                                                  # Timeout = 5 --> Wait at most 5 seconds for the server response.
        if response.status_code == 200:           # Our response object does have a attribute of status_code
            return response.json()
        else:
            print(f"Pokemon '{name}' not found!")

    except requests.exceptions.Timeout:
        print("The reqest took too long!")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

pokemon_name = input("Enter pokemon name: ").lower()

pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"\nName: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")