import json
from objects.pokemon import Pokemon
from objects.trainer import Trainer
from objects.p_t_pair import P_T_Pair
from objects.type import Type
from utils.constants import *


def _get_dict_from_json(json_dir: str):
    poke_data_file = open(json_dir)
    poke_data = json.load(poke_data_file)
    poke_data_file.close()
    return poke_data


def _parse_poke_data(poke_data):
    pokemons, pokemons_trainers, pokemons_types = set(), set(), set()
    trainers = dict()  # {trainer: trainerId}
    types = dict()  # {type: trainerId}
    trainer_id, type_id = 1, 1
    for p in poke_data:
        pokemon = Pokemon(p[P_ID], p[P_NAME], p[P_HEIGHT], p[P_WEIGHT])
        pokemons.add(pokemon)
        type = Type(type_id, p[P_TYPE])
        if type not in types:
            types[type] = type_id
            type_id += 1
        pokemons_types.add(P_T_Pair(pokemon.id, types[type]))
        for t in p[P_TRAINER]:
            trainer = Trainer(trainer_id, t[T_NAME], t[T_TOWN])
            if trainer not in trainers:
                trainers[trainer] = trainer_id
                trainer_id += 1
            pokemons_trainers.add(P_T_Pair(pokemon.id, trainers[trainer]))
    return pokemons, trainers, pokemons_trainers, types, pokemons_types


def parse(json_dir: str):
    poke_data = _get_dict_from_json(json_dir)
    return _parse_poke_data(poke_data)
