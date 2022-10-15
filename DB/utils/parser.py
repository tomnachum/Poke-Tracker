from utils.constants import *
import json
from Objects.pokemon import Pokemon
from Objects.trainer import Trainer
from Objects.pokemon_trainer_pair import P_T_Pair


def _get_dict_from_json(json_dir: str):
    poke_data_file = open(json_dir)
    poke_data = json.load(poke_data_file)
    poke_data_file.close()
    return poke_data


def _parse_poke_data(poke_data):
    pokemons, pokemons_trainers = set(), set()
    trainers = dict()  # {trainer: trainerId}
    trainer_id = 1
    for p in poke_data:
        pokemon = Pokemon(p[P_ID], p[P_NAME], p[P_TYPE], p[P_HEIGHT], p[P_WEIGHT])
        pokemons.add(pokemon)
        for t in p[P_TRAINER]:
            trainer = Trainer(trainer_id, t[T_NAME], t[T_TOWN])
            if trainer not in trainers:
                trainers[trainer] = trainer_id
                trainer_id += 1
            pokemons_trainers.add(P_T_Pair(pokemon.id, trainers[trainer]))
    return pokemons, trainers, pokemons_trainers


def parse(json_dir: str):
    poke_data = _get_dict_from_json(json_dir)
    return _parse_poke_data(poke_data)
