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


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
