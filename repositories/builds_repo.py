from repositories.db import get_pool
from psycopg.rows import dict_row
from datetime import datetime

def get_all_builds_from_user_id(user_id: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT a.build_id, a.build_name, a.refer_url, a.build_timestamp, a.is_private, a.total_price
                            FROM builds a JOIN users b on a.user_id = b.user_id
                            WHERE b.user_id = %s
                           ''', [user_id])
            return cursor.fetchall()

def get_all_users_for_table():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT user_id, username, email, hashed_password, is_admin,
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

def does_build_name_exist(build_name: str) -> bool:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT build_id
                            FROM builds
                            WHERE build_name = %s
                           ''', [build_name])
            build_id = cursor.fetchone()
            return build_id is not None

def get_total_build_price(build_name: str) -> bool:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SUM(price)
                            FROM components a JOIN parts b WHERE a.part_id = b.part_id JOIN build c WHERE c.build_id = a.build_id 
                            WHERE build_name = %s
                           ''', [build_name])
            total_price = cursor.fetchone()
            return total_price

def create_user(username: str, hashed_password: str, email: str, is_admin: bool = False):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO users (username, email, hashed_password, is_admin) 
                            VALUES (%(username)s, %(email)s, %(hashed_password)s, %(is_admin)s)
                            RETURNING image_id
                           ''', {'username': username, 'email': email, 'hashed_password': hashed_password, 'is_admin': is_admin})
            user_id = cursor.fetchone()
            if user_id is None:
                raise Exception('Failed to create user')
            return {
                'user_id': user_id,
                'username': username
            }

def create_build(parts: dict, build_name: str, is_private: bool, user_id: int):
    build_timestamp = datetime.now()
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO builds (build_name, build_timestamp, is_private, user_id) 
                            VALUES (%(build_name)s, %(build_timestamp)s, %(is_private)s, %(user_id)s)
                            RETURNING build_id
                           ''', {'build_name': build_name, 'build_timestamp': build_timestamp, 'is_private': is_private, 'user_id': user_id})
            res = cursor.fetchone()
            if not res:
                raise Exception('Failed to create build')
            return res[0]
    