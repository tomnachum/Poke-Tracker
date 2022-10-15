from utils.constants import *
import json
from Objects.pokemon import Pokemon
from Objects.trainer import Trainer


def _get_dict_from_json(json_dir: str):
    poke_data_file = open(json_dir)
    poke_data = json.load(poke_data_file)
    poke_data_file.close()
    return poke_data


def _parse_poke_data(poke_data):
    pokemons, trainers, pokemons_trainers = set(), set(), set()
    trainer_id = 1
    for p in poke_data:
        p_id = p[P_ID]
        pokemon = Pokemon(p_id, p[P_NAME], p[P_TYPE], p[P_HEIGHT], p[P_WEIGHT])
        pokemons.add(pokemon)
        if len(p[P_TRAINER]) == 0:
            pokemons_trainers.add((p_id, None))
        for t in p[P_TRAINER]:
            trainer = Trainer(trainer_id, t[T_NAME], t[T_TOWN])
            trainers.add(trainer)
            pokemons_trainers.add((p_id, trainer_id))
            trainer_id += 1
    return pokemons, trainers, pokemons_trainers


def parse(json_dir: str):
    poke_data = _get_dict_from_json(json_dir)
    return _parse_poke_data(poke_data)
