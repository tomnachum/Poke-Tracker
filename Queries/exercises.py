import pymysql

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


print(find_owners("bulbasaur", "", "Dantha"))


def find_roster(trainer_name="", pokemon_id="", pokemon_type=""):
    if not (pokemon_id == ""):
        pokemon_id = f" AND p.p_id = {pokemon_id}"
    if not (pokemon_type == ""):
        pokemon_type = f" AND p.type = '{pokemon_type}'"
    if not (trainer_name == ""):
        trainer_name = f" AND t.name = '{trainer_name}'"
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT DISTINCT p.name
                    FROM pokemons AS p JOIN pokemons_trainers AS pt JOIN trainers AS t
                    ON p.p_id = pt.p_id AND t.t_id = pt.t_id
                    WHERE 1 = 1 {trainer_name}{pokemon_id}{pokemon_type}
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return [e["name"] for e in result]
    except Exception as e:
        print(e)


# print(find_roster("", "", "grass"))


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
