import os
from psycopg_pool import ConnectionPool

pool = None

def get_pool():
    global pool
    if pool is None:
        pool = ConnectionPool(
            #Make sure to have .env with DATABASE_URL=""
            conninfo=os.getenv('DATABASE_URL', ''),
        )
    return pool
