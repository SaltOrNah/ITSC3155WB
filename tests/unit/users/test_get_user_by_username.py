from app import app
import unittest
from repositories import builds_repo

def test_get_user_by_username():
    #Using last test
    test_user = builds_repo.get_user_by_username("Example2")
    assert test_user['username'] == 'Example2'