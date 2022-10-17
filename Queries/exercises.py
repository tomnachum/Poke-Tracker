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


def find_owners(pokemon_name):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT DISTINCT t.name
                    FROM pokemons AS p JOIN pokemons_trainers AS pt JOIN trainers AS t
                    ON p.p_id = pt.p_id AND t.t_id = pt.t_id
                    WHERE p.name = '{pokemon_name}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return [e["name"] for e in result]
    except Exception as e:
        print(e)


def find_roster(trainer_name):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT DISTINCT p.name
                    FROM pokemons AS p JOIN pokemons_trainers AS pt JOIN trainers AS t
                    ON p.p_id = pt.p_id AND t.t_id = pt.t_id
                    WHERE t.name = '{trainer_name}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return [e["name"] for e in result]
    except Exception as e:
        print(e)


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
