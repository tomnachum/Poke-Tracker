import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


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


def get_types():
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT *
                    FROM types
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return {t["name"]: t["ty_id"] for t in result}
    except Exception as e:
        print(e)


def add_type(type_name: str):
    if type_name in get_types():
        return
    try:
        with connection.cursor() as cursor:
            query = f"""
                    INSERT INTO types VALUES
                    (null, '{type_name}')
                    """
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(e)


def add_pokemon_type_pair(p_id, ty_id):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    INSERT INTO pokemons_types VALUES
                    ({p_id}, {ty_id})
                    """
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(e)


def get_type_id(type_name):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT ty_id
                    FROM types
                    WHERE name = '{type_name}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return result[0]["ty_id"]
    except Exception as e:
        print(e)


def add_trainer_to_DB(name, town):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    INSERT INTO trainers VALUES
                    (null, '{name}', '{town}')
                    """
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(e)


def get_trainer_id(trainer_name: str):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT t_id
                    FROM trainers
                    WHERE name = '{trainer_name}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return result[0]["t_id"]
    except Exception as e:
        print(e)
