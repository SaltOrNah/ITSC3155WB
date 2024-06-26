from repositories.db import get_pool
from psycopg.rows import dict_row
from datetime import datetime

def get_all_builds_from_user_id(user_id: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT a.build_id, a.build_name, a.build_timestamp, a.is_private
                            FROM builds a JOIN users b ON a.user_id = b.user_id
                            WHERE b.user_id = %s
                           ''', [user_id])
            return cursor.fetchall()
        
def get_all_saves_from_user_id(user_id: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT b.*
                            FROM user_builds ub
                            JOIN builds b ON ub.build_id = b.build_id
                            WHERE ub.user_id = %s
                           ''', [user_id])
            return cursor.fetchall()

def get_all_users_for_table():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT user_id, username, hashed_password, is_admin
                            FROM users
                           ''')
            return cursor.fetchall()

def get_all_parts_for_table():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT part_id, part_name, part_type, brand, price, rating
                            FROM parts
                           ''')
            return cursor.fetchall()

def get_user_by_id(user_id: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT user_id, username, hashed_password, is_admin
                            FROM users
                            WHERE user_id = %s
                            ''', [user_id])
            return cursor.fetchone()

def get_part_by_id(part_id: int) -> dict:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT *
                            FROM parts
                            WHERE part_id = %s
                            ''', [part_id])
            return cursor.fetchone()
        
def get_build_by_id(build_id: int) -> dict:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT *
                            FROM builds
                            WHERE build_id = %s
                           ''', [build_id])
            return cursor.fetchone()

def get_all_parts_by_part_type(part_type: str):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT part_id, part_name, part_type, brand, price, rating
                            FROM parts
                            WHERE part_type = %s
                           ''', [part_type])
            return cursor.fetchall()

def get_component_parts_by_search(search: str, part_type: str):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT part_id, part_name, part_type, brand, price, rating
                            FROM parts
                            WHERE LOWER(part_name) LIKE %(search)s AND part_type = %(part_type)s
                           ''', {'search': f'%{search}%', 'part_type': part_type})
            return cursor.fetchall()

def get_all_parts_by_search(search: str):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT part_id, part_name, part_type, brand, price, rating
                            FROM parts
                            WHERE LOWER(part_name) LIKE %(search)s
                           ''', {'search': f'%{search}%'})
            return cursor.fetchall()

def get_all_builds_by_build_type(build_type: str):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT *
                            FROM builds
                            WHERE build_type = %s
                           ''', [build_type])
            return cursor.fetchall()

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
                            SELECT SUM(price)
                            FROM components a JOIN parts b ON a.part_id = b.part_id JOIN builds c ON c.build_id = a.build_id 
                            WHERE build_name = %s
                           ''', [build_name])
            total_price = cursor.fetchone()
            return total_price

def create_user(username: str, hashed_password: str, is_admin: bool = False):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO users (username, hashed_password, is_admin) 
                            VALUES (%(username)s, %(hashed_password)s, %(is_admin)s)
                            RETURNING user_id
                           ''', {'username': username, 'hashed_password': hashed_password, 'is_admin': is_admin})
            user_id = cursor.fetchone()
            if user_id is None:
                raise Exception('Failed to create user')
            return {
                'user_id': user_id,
                'username': username
            }

def get_user_by_username(username: str)-> None:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT
                                user_id,
                                username,
                                hashed_password
                            FROM
                                users
                            WHERE username = %s
                            ''', [username])
            user = cursor.fetchone()
            return user

def create_part(part_name: dict, part_type: str, part_image: str, part_url: str, brand: str, price, rating) -> int:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO parts (part_name, part_type, part_image, part_url, brand, price, rating) 
                            VALUES (%(part_name)s, %(part_type)s, %(part_image)s, %(part_url)s, %(brand)s, %(price)s, %(rating)s)
                            RETURNING part_id
                           ''', {'part_name': part_name, 'part_type': part_type, 'part_image': part_image, 'part_url': part_url, 'brand': brand, 'price': price, 'rating': rating})
            res = cursor.fetchone()
            if not res:
                raise Exception('Failed to create part')
            return res[0]

def create_build(parts: dict, build_type: str, build_name: str, is_private: bool, user_id: int, build_image: str = 'https://ralfvanveen.com/wp-content/uploads//2021/06/Placeholder-_-Begrippenlijst.svg'):
    build_timestamp = datetime.now()
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO builds (build_name, build_type, build_timestamp, is_private, user_id, build_image) 
                            VALUES (%(build_name)s, %(build_type)s, %(build_timestamp)s, %(is_private)s, %(user_id)s, %(build_image)s)
                            RETURNING build_id
                           ''', {'build_name': build_name, 'build_type': build_type, 'build_timestamp': build_timestamp, 'is_private': is_private, 'user_id': user_id, 'build_image': build_image})
            res = cursor.fetchone()
            if not res:
                raise Exception('Failed to create build')
            temp_list = []
            build_id = res[0]
            for part in parts:
                part_id = part['part_id']
                temp_list.append(part_id)
                amount = temp_list.count(part_id)
                if amount > 1:
                    cursor.execute('''
                                    UPDATE components
                                    SET quantity = %(amount)s
                                    WHERE part_id = %(part_id)s
                                   ''', {'amount': amount, 'part_id': part_id})
                else:
                    cursor.execute('''
                                    INSERT INTO components (part_id, build_id, quantity) 
                                    VALUES (%(part_id)s, %(build_id)s, %(quantity)s)
                                   ''', {'part_id': part_id, 'build_id': build_id, 'quantity': 1})
            del temp_list
            return build_id

def save_build(build_id: int, user_id: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            INSERT INTO user_builds (user_id, build_id)
                            SELECT %(user_id)s, %(build_id)s
                            WHERE NOT EXISTS (
                            SELECT 1
                            FROM user_builds
                            WHERE user_id = %(user_id)s AND build_id = %(build_id)s);
                           ''', {'build_id': build_id, 'user_id': user_id})

def remove_saved_build(build_id: int, user_id: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            DELETE FROM user_builds
                            WHERE user_id = %(user_id)s AND build_id = %(build_id)s;
                           ''', {'build_id': build_id, 'user_id': user_id})
            conn.commit()

def get_all_parts_by_build_id(build_id: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT p.part_id, p.part_name, p.part_type, p.brand, p.price, p.rating
                            FROM components c
                            JOIN parts p ON c.part_id = p.part_id
                            WHERE c.build_id = %s
                           ''', [build_id])
            return cursor.fetchall()
        
def delete_build_by_id(build_id: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            # Delete associated user-build records first
            cursor.execute('''
                            DELETE FROM user_builds
                            WHERE build_id = %s
                           ''', [build_id])
            # Delete associated components first
            cursor.execute('''
                            DELETE FROM components
                            WHERE build_id = %s
                           ''', [build_id])
            # Then delete the build
            cursor.execute('''
                            DELETE FROM builds
                            WHERE build_id = %s
                           ''', [build_id])
            conn.commit()

def for_testing_only_delete_part(part_id: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            DELETE FROM parts
                            WHERE part_id = %s
                           ''', [part_id])
            conn.commit()

def for_testing_only_delete_user(username: int):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                            DELETE FROM users
                            WHERE username = %s
                           ''', [username])
            conn.commit()