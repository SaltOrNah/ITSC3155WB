from app import app
import unittest
from repositories import builds_repo

def test_get_user_by_id():
    #Using last test
    users = builds_repo.get_all_users_for_table()
    test_user = builds_repo.get_user_by_username("Example2")
    assert test_user['user_id'] == builds_repo.get_user_by_id(test_user['user_id'])['user_id']