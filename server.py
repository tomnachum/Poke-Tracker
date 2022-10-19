from fastapi import FastAPI, Request, Response
import uvicorn
import requests
from queries.queries import *
from queries.exercises import *

app = FastAPI()


@app.get("/pokemons/{name}")
def get_pokemon(name: str):
    pokemon_response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{name}").json()
    types = [e["type"]["name"].lower() for e in pokemon_response["types"]]
    p_id = get_pokemon_id(name)
    for type in types:
        add_type(type)
        ty_id = get_type_id(type)
        add_pokemon_type_pair(p_id, ty_id)
    # TODO: return the pokemon data
    return {"id": p_id, "types": types}

# can return all the pokemons from some type


@app.get('/pokemons')
async def get_all_the_trainer_pokemons(trainer_name="", pokemon_id="", pokemon_type=""):
    return find_roster(trainer_name, pokemon_id, pokemon_type)



@app.get('/trainers')
async def get_all_the_pokemon_trainers(pokemon_name="", trainer_id="", trainer_name=""):
    return find_owners(pokemon_name, trainer_id, trainer_name)


# adds a new trainer
# with the following information
# given by the client: name, town.

@app.post("/trainers")
async def add_trainer(request: Request):
    req = await request.json()
    add_trainer_to_DB(req["name"], req["town"])
    return {"message": "Trainer added successfully"}


@app.delete("/pokemons/{p_name}/trainers/{t_name}")
def delete_pokemon_of_trainer(p_name, t_name):
    p_id = get_pokemon_id(p_name)
    t_id = get_trainer_id(t_name)
    remove_pokemon_from_trainer(p_id, t_id)
    return {"message": "Pokemon was removed from trainer successfully"}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
