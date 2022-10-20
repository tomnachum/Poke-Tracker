import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


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
