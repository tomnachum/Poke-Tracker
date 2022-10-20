import pymysql
from queries.pokemon_queries import get_pokemon_name_by_id, get_all_pokemons
from queries.pokemons_trainers_queries import get_pokemons_names_by_trainer
from queries.pokemons_types_queries import get_pokemons_names_by_type

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


def find_heaviest():
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT name
                    FROM pokemons
                    WHERE weight = (
                            SELECT MAX(weight)
                            from pokemons
                        );
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return result[0]["name"]
    except Exception as e:
        print(e)


def find_by_type(pokemon_type):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT DISTINCT name
                    FROM pokemons
                    WHERE type = '{pokemon_type}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return [e["name"] for e in result]
    except Exception as e:
        print(e)


def find_owners(pokemon_name="", trainer_id="", trainer_name=""):
    if not (pokemon_name == ""):
        pokemon_name = f" AND p.name = '{pokemon_name}'"
    if not (trainer_id == ""):
        trainer_id = f" AND t.t_id = '{trainer_id}'"
    if not (trainer_name == ""):
        trainer_name = f" AND t.name = '{trainer_name}'"
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT DISTINCT t.name
                    FROM pokemons AS p JOIN pokemons_trainers AS pt JOIN trainers AS t
                    ON p.p_id = pt.p_id AND t.t_id = pt.t_id
                    WHERE 1 = 1 {pokemon_name}{trainer_id}{trainer_name}
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return [e["name"] for e in result]
    except Exception as e:
        print(e)


def find_roster(trainer_name="", pokemon_type=""):
    pokemons_of_trainer = set(get_pokemons_names_by_trainer(trainer_name))
    pokemons_of_type = set(get_pokemons_names_by_type(pokemon_type))
    print(pokemons_of_trainer, pokemons_of_type)
    if trainer_name == "" and pokemon_type == "":
        return list(set(get_all_pokemons()))
    elif trainer_name != "" and pokemon_type == "":
        return list(pokemons_of_trainer)
    elif trainer_name == "" and pokemon_type != "":
        return list(pokemons_of_type)
    else:
        intersection = pokemons_of_trainer.intersection(pokemons_of_type)
        return list(intersection)


def find_most_owned():
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT DISTINCT name
                    FROM pokemons AS p JOIN pokemons_trainers AS pt
                    ON p.p_id = pt.p_id
                    GROUP BY p.p_id
                    HAVING COUNT(t_id) >= ALL (
                                    SELECT COUNT(t_id)
                                    FROM pokemons_trainers
                                    GROUP BY p_id
                        )
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return [e["name"] for e in result]
    except Exception as e:
        print(e)


# eden
# def add_trainer_to_db(trainer):
#     try:
#         with connection.cursor() as cursor:
#             query = f"""
#                     INSERT INTO trainers VALUES
#                     {",".join(str(trainer))}
#                     """
#             cursor.execute(query)
#             connection.commit()
#     except Exception as trainer:
#         print(f"Error in initializing trainers table")
#         print(trainer)
