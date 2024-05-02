from app import app
import unittest
from repositories import builds_repo

def test_get_user_by_username():
    user= None
    if(builds_repo.does_username_exist("Example2")):
        builds_repo.for_testing_only_delete_user("Example2")
    user = builds_repo.create_user("Example2", "hashed_password", False)
    
    test_user = builds_repo.get_user_by_username("Example2")

    assert user['username'] == 'Example2'