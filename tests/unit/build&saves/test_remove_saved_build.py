from app import app
import unittest
from repositories import builds_repo

def test_remove_saved_build():
    part = builds_repo.get_all_parts_for_table()
    if(len(part) <= 0):
        builds_repo.create_part('ARCTIC Liquid Freezer III 56.3 CFM Liquid CPU Cooler', 'cooling', 'cooling_image_4.jpg', 'https://example.com/cooling4', 'Brand D', 94.99, 4.2)
        part = builds_repo.get_all_parts_for_table()

    if(builds_repo.does_username_exist("Example1")):
        builds_repo.for_testing_only_delete_user("Example1")
    user = builds_repo.create_user("Example1", "hashed_password", False)
    user = builds_repo.get_user_by_id(user['user_id'][0])

    build_id = builds_repo.create_build(part, "gaming", "Great", False, 1, "")

    builds_repo.save_build(build_id, user['user_id'])
    user_builds = builds_repo.get_all_saves_from_user_id(user['user_id'])
    builds_repo.remove_saved_build(build_id, user['user_id'])
    new_user_builds = builds_repo.get_all_saves_from_user_id(user['user_id'])

    builds_repo.for_testing_only_delete_user("Example1")
    builds_repo.delete_build_by_id(build_id)
    assert user_builds != new_user_builds