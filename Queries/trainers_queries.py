import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


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
