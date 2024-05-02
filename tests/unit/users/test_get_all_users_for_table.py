from app import app
import unittest
from repositories import builds_repo

def test_get_all_users_for_table():
    user= None
    if(builds_repo.does_username_exist("Example2")):
        builds_repo.for_testing_only_delete_user("Example2")
    user = builds_repo.create_user("Example2", "hashed_password", False)

    users = builds_repo.get_all_users_for_table()
    found_user = False
    for u in users:
        if u['username'] == 'Example2':
            found_user = True

    builds_repo.for_testing_only_delete_user("Example2")
    assert found_user