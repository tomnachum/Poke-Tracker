from fastapi import FastAPI, Request, Response
import uvicorn
import requests
from queries.queries import *
from queries.exercises import *

app = FastAPI()


def add_types_to_DB(p_name, p_id):
    pokemon_response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{p_name}"
    ).json()
    types = [e["type"]["name"].lower() for e in pokemon_response["types"]]
    for type in types:
        add_type(type)
        ty_id = get_type_id(type)
        add_pokemon_type_pair(p_id, ty_id)
    return types


@app.get("/pokemons/{name}")
def get_pokemon(name: str):
    p_id = get_pokemon_id(name)
    types = add_types_to_DB(name, p_id)
    pokemon_data = get_pokemon_by_id(p_id)
    return {"pokemon": pokemon_data, "types": types}


@app.get("/trainers")
async def get_all_the_pokemon_trainers(pokemon_name="", trainer_id="", trainer_name=""):
    # can return all the pokemons from some type
    return find_owners(pokemon_name, trainer_id, trainer_name)


@app.post("/trainers")
async def add_trainer(request: Request):
    # adds a new trainer
    # with the following information
    # given by the client: name, town.
    req = await request.json()
    add_trainer_to_DB(req["name"], req["town"])
    return {"message": "Trainer added successfully"}


@app.delete("/pokemons/{p_name}/trainers/{t_name}")
def delete_pokemon_of_trainer(p_name, t_name):
    p_id = get_pokemon_id(p_name)
    t_id = get_trainer_id(t_name)
    remove_pokemon_from_trainer(p_id, t_id)
    return {"message": "Pokemon was removed from trainer successfully"}


@app.get("/pokemons")
async def get_all_the_trainer_pokemons(trainer_name="", pokemon_id="", pokemon_type=""):
    return find_roster(trainer_name, pokemon_id, pokemon_type)


@app.put("/evolve/trainers/{t_name}/pokemons/{p_name}")
def evlove(t_name, p_name):
    old_p_id = get_pokemon_id(p_name)
    trainer_have_this_pokemon = find_roster(t_name, old_p_id, "")
    if trainer_have_this_pokemon == []:
        return {"Message": "This trainer does not have that pokemon"}
    pokemon_response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{p_name}"
    ).json()
    species = pokemon_response["species"]
    evolution_chain = requests.get(species["url"]).json()
    evolution_url = evolution_chain["evolution_chain"]["url"]

    chain = requests.get(evolution_url).json()["chain"]
    evolves_to = chain["evolves_to"]
    c = chain["species"]["name"]
    # if chain["species"]["name"] != p_name:
    while evolves_to != [] and c != p_name:
        evolves_to = evolves_to[0]
        c = evolves_to["evolves_to"][0]["species"]["name"]
        evolves_to["evolves_to"]

    if evolves_to == []:
        return {"Message": "No evolves avilable"}
    if evolves_to[0]["species"]["name"] == p_name:
        evolves_to = evolves_to[0]["evolves_to"]

    evolve = evolves_to[0]["species"]["name"]
    new_p_id = get_pokemon_id(evolve)
    t_id = get_trainer_id(t_name)
    update_pokemon_trainer(old_p_id, t_id, new_p_id)
    return {"Message": "The evolve succeeded", "Evolve to": evolve}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
