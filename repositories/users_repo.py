from repositories.db import get_pool

def get_all_images_for_table():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                           SELECT * 
                           FROM parts''')
            return cursor.fetchall()