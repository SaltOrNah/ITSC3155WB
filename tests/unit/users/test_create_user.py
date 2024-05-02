from app import app
import unittest
from repositories import builds_repo

def test_create_user():
    user= None
    if(builds_repo.does_username_exist("Example2")):
        builds_repo.for_testing_only_delete_user("Example2")
    user = builds_repo.create_user("Example2", "hashed_password", False)

    builds_repo.for_testing_only_delete_user("Example2")
    assert user['username'] == "Example2"