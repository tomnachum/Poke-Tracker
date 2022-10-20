import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


def get_pokemon_by_id(p_id):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT *
                    FROM pokemons
                    WHERE p_id = '{p_id}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)


def get_pokemon_id(pokemon_name: str):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT p_id
                    FROM pokemons
                    WHERE name = '{pokemon_name}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return result[0]["p_id"]
    except Exception as e:
        print(e)
