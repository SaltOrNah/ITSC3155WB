from app import app
import unittest
from repositories import builds_repo

def test_create_user():
    if("Example2" == builds_repo.does_username_exist("Example2")):
        builds_repo.create_user("Example2", "hashed_password")
    user = builds_repo.get_user_by_username("Example2")

    assert user['username'] == "Example2"