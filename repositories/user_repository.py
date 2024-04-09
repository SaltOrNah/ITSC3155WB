from repositories.db import get_pool
from typing import Any

def does_username_exist(username: str) -> bool:
    pool = get_pool()
    with pool.connection() as conn: 
        with conn.curser() as cur:
            cur.execute('''
                        SELECT
                            user_id
                        FROM
                            app_user
                        WHERE username = %s

                        ''', [username])
            user_id = cur.fetchone()
            return user_id is not None
        
def create_user(username:str, password: str) -> dict[str, Any]:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(''' 
                        INSERT INTO app_user (username, password)
                        VALUES (%s, %s)
                        RETURNING user_id
                        ''')
            user_id = cur.fetchone()
            if user_id is None:
                raise Exception('Failed to create user')
            return {
                'user_id': user_id,
                'username': username
            }