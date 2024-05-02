from app import app
import unittest
from repositories import builds_repo

def test_does_username_exist():
    #Using last test
    assert builds_repo.does_username_exist("Example2")