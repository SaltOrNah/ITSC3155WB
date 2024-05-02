from app import app
import unittest
from repositories import builds_repo

def test_create_part():
    part1 = builds_repo.get_part_by_id(1)
    parts = builds_repo.get_all_parts_for_table()
    if(len(parts) <= 0):
        part_id = builds_repo.create_part('ARCTIC Liquid Freezer III 56.3 CFM Liquid CPU Cooler', 'cooling', 'cooling_image_4.jpg', 'https://example.com/cooling4', 'Brand D', 94.99, 4.2)
        part1 = builds_repo.get_part_by_id(part_id)
    part2 = builds_repo.get_part_by_id(-1)
    assert part1 is not None
    assert part2 is None