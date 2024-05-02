from app import app
import unittest
from repositories import builds_repo

def test_get_all_saves_from_user_id():
    part = builds_repo.get_all_parts_for_table()
    if(len(part) <= 0):
        builds_repo.create_part('ARCTIC Liquid Freezer III 56.3 CFM Liquid CPU Cooler', 'cooling', 'cooling_image_4.jpg', 'https://example.com/cooling4', 'Brand D', 94.99, 4.2)
        part = builds_repo.get_all_parts_for_table()
    user = builds_repo.get_user_by_username("Example")
    if(user is None):
        user = builds_repo.create_user("Example", "password")
    build_id = builds_repo.create_build(part, "gaming", "Great", False, user['user_id'])
    
    builds_repo.save_build(build_id, user['user_id'])
    user_builds = builds_repo.get_all_saves_from_user_id(user['user_id'])

    builds_repo.delete_build_by_id(build_id)
    assert len(user_builds) > 0
    