from fastapi import FastAPI, Request, Response
import uvicorn
import requests
from queries.queries import *

app = FastAPI()


@app.get("/pokemons/{name}")
def get_pokemon(name: str):
    pokemon_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").json()
    types = [e["type"]["name"].lower() for e in pokemon_response["types"]]
    p_id = get_pokemon_id(name)
    for type in types:
        add_type(type)
        ty_id = get_type_id(type)
        add_pokemon_type_pair(p_id, ty_id)
    # TODO: return the pokemon data
    return {"id": p_id, "types": types}


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
