import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


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
