import pymysql
from queries.types_queries import get_type_id

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


def get_pokemons_names_by_type(type):
    ty_id = get_type_id(type)
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT DISTINCT p.name
                    FROM pokemons AS p JOIN pokemons_types AS pt
                    ON p.p_id = pt.p_id
                    WHERE pt.ty_id = '{ty_id}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return [e["name"] for e in result]
    except Exception as e:
        print(e)
