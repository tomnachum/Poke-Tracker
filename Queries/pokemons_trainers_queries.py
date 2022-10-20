import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


def remove_pokemon_from_trainer(p_id, t_id):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    DELETE FROM pokemons_trainers
                    WHERE p_id = '{p_id}' AND t_id = '{t_id}'
                    """
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(e)


def update_pokemon_trainer(old_p_id, t_id, new_p_id):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    UPDATE pokemons_trainers
                    SET p_id = '{new_p_id}'
                    WHERE t_id = '{t_id}' AND p_id = '{old_p_id}'
                    """
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(e)
