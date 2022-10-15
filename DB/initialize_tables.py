import imp
import pymysql
from utils.parser import parse
from utils.constants import POKE_DATA_DIR

pokemons, trainers = parse(POKE_DATA_DIR)
print(pokemons)
print(trainers)
