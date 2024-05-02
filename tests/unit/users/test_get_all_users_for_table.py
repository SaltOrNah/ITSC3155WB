from app import app
import unittest
from repositories import builds_repo

def test_get_all_users_for_table():
    #Using last test
    users = builds_repo.get_all_users_for_table()
    found_user = False
    for u in users:
        if u['username'] == 'Example2':
            found_user = True
    assert found_user