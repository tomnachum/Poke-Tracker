from cmath import asinh
import re
from fastapi.responses import FileResponse
from fastapi import FastAPI, Request
import uvicorn
import requests

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from Queries.exercises import add_trainer_to_db, find_owners, find_roster


app = FastAPI()


# app.mount("/frontend", StaticFiles(directory="backend/frontend"), name="frontend")


# @app.get("/")
# async def get_client():
#     return FileResponse('backend\\frontend\index.html')


# @app.get('/pokemons/{trainer_name}')
# async def get_trainer_pokemons(trainer_name,):
#     return await find_roster(trainer_name)

# /pokemon/ash
# /pokemon/grass
# /pokemon?trainer=ash&type=grass


@app.get('/pokemons')
async def get_trainer_pokemons_query_params(trainer_name="", pokemon_id="", pokemon_type=""):
    return find_roster(trainer_name, pokemon_id, pokemon_type)


@app.get('/trainers')
async def get_pokemon_trainers_query_params(pokemon_name="", trainer_id="", trainer_name=""):
    return find_owners(pokemon_name, trainer_id, trainer_name)


@app.post("/trainers")
async def add_trainer(trainerRequest: Request):
    trainer = await trainerRequest.json()
    add_trainer_to_db(trainer)
    return


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=4000, reload=True)
