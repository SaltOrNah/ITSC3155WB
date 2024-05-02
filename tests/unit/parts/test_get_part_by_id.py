from app import app
import unittest
from repositories import builds_repo

def test_get_part_by_id():
    part_id = builds_repo.create_part('ARCTIC Liquid Freezer III 56.3 CFM Liquid CPU Cooler', 'cooling', 'cooling_image_4.jpg', 'https://example.com/cooling4', 'Brand D', 94.99, 4.2)
    
    part = builds_repo.get_part_by_id(part_id)

    builds_repo.for_testing_only_delete_part(part_id)
    assert part['part_id'] == part_id
    