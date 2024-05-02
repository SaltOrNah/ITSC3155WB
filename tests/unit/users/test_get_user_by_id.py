from app import app
import unittest
from repositories import builds_repo

def test_get_user_by_id():
    user= None
    if(builds_repo.does_username_exist("Example2")):
        builds_repo.for_testing_only_delete_user("Example2")
    user = builds_repo.create_user("Example2", "hashed_password", False)['user_id'][0]
    user_id = builds_repo.get_user_by_id(user)
    
    builds_repo.for_testing_only_delete_user("Example2")
    assert user == user_id['user_id']