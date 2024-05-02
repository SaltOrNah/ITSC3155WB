from app import app
import unittest
from repositories import builds_repo

def test_does_username_exist():
    user= None
    if(builds_repo.does_username_exist("Example2")):
        builds_repo.for_testing_only_delete_user("Example2")
    user = builds_repo.create_user("Example2", "hashed_password", False)
    exist = builds_repo.does_username_exist(user['username'])

    builds_repo.for_testing_only_delete_user("Example2")
    assert exist