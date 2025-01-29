import requests


def main():
    base_url="https://pokeapi.co/api/v2/"

    def get_pokemon_info(name):
        url=f"{base_url}/pokemon/{name}"
        response=requests.get(url)

        if response.status_code==200:
            pokemon_data=response.json()
            return pokemon_data
        else:
            print(f"Failed to retrieve data for {name}. Status code: {response.status_code}")
            return None
        
    pokemon_name=input("Enter the name of the pokemon ")

    data=get_pokemon_info(pokemon_name)

    if data:
        print(f"Name: {data["name"].capitalize()}")
        print(f"Id: {data['id']}")
        print(f"Type: {data["types"][0]['type']['name']}")
        print(f"Weight: {data['weight']}")
        print(f"Height: {data['height']}")
    else:
        print("Pokemon not found")

if __name__=="__main__":
    main()