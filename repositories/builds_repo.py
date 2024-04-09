from repositories.db import get_pool
from psycopg.rows import dict_row
from datetime import datetime

def get_all_builds_from_user_id(user_id: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT a.build_id, a.build_name, a.refer_url, a.time_created, a.is_private, a.total_price
                            FROM builds a JOIN users b on a.user_id = b.user_id
                            WHERE b.user_id = %s
                           ''', [user_id])
            return cursor.fetchall()

def get_all_users_for_table():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT user_id, email, user_name, hashed_password, is_admin,
                            FROM users
                           ''')
            return cursor.fetchall()

def get_all_parts_for_table():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT part_id, part_name, part_type, brand, price, rating,
                            FROM parts
                           ''')
            return cursor.fetchall()

def get_user_by_id(user_id: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT user_id, email, user_name, hashed_password, is_admin,
                            FROM users
                            WHERE user_id = %s
                           ''', [user_id])
            return cursor.fetchone()
        
def get_username_by_id(email: str):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT user_id, email, username, hashed_password, is_admin,
                            FROM users
                            WHERE user_id = %s
                           ''', [email])
            return cursor.fetchone()

def does_username_exist(username: str) -> bool:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT user_id
                            FROM users
                            WHERE username = %s
                           ''', [username])
            user_id = cursor.fetchone()
            return user_id is not None

def create_user(username: str, hashed_password: str, email: str, is_admin: bool = False):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO users (username, email, hashed_password, is_admin) 
                            VALUES (%(username)s, %(password)s, %(email)s, %(is_admin)s)
                            RETURNING image_id
                           ''', {'username': username, 'hashed_password': hashed_password, 'email': email, 'is_admin': is_admin})
            user_id = cursor.fetchone()
            if user_id is None:
                raise Exception('Failed to create user')
            return {
                'user_id': user_id,
                'username': username
            }

# def create_build(parts: dict, build_name: str, is_private: bool, user_id: int):
#     build_timestamp = datetime.now()
#     refer_url = f'/{get_username_by_id(user_id)['username']}/{build_name}'
#     pool = get_pool()
#     with pool.connection() as conn:
#         with conn.cursor() as cursor:
#             cursor.execute('''
#                             INSERT INTO images (image_timestamp, caption, link, user_id) 
#                             VALUES (%(image_timestamp)s, %(caption)s, %(link)s, %(user_id)s)
#                             RETURNING image_id
#                            ''', {'image_timestamp': image_timestamp, 'caption': caption, 'link': link, 'user_id': user_id})
#             res = cursor.fetchone()
#             if not res:
#                 raise Exception('Failed to create build')
#             return res[0]