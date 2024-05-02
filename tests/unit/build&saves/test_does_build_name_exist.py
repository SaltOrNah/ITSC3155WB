from app import app
import unittest
from repositories import builds_repo

def test_does_build_name_exist():
    part = builds_repo.get_all_parts_for_table()
    if(len(part) <= 0):
        part_id = builds_repo.create_part('ARCTIC Liquid Freezer III 56.3 CFM Liquid CPU Cooler', 'cooling', 'cooling_image_4.jpg', 'https://example.com/cooling4', 'Brand D', 94.99, 4.2)
        part = builds_repo.get_all_parts_for_table()
        
    build_id = builds_repo.create_build(part, "gaming", "Great", False, 1, "")
    
    build1 = builds_repo.does_build_name_exist("Great")
    #names can't be empty
    build2 = builds_repo.does_build_name_exist("")

    builds_repo.delete_build_by_id(build_id)
    assert build1 == True
    assert build2 == False
    