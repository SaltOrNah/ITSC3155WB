from app import app
import unittest
from repositories import builds_repo

def test_get_all_parts_by_search():
    part = builds_repo.get_all_parts_for_table()
    if(len(part) <= 0):
        builds_repo.create_part('ARCTIC Liquid Freezer III 56.3 CFM Liquid CPU Cooler', 'cooling', 'cooling_image_4.jpg', 'https://example.com/cooling4', 'Brand D', 94.99, 4.2)
        part = builds_repo.get_all_parts_for_table()
    parts = builds_repo.get_all_parts_by_search("Liquid")

    found_part = False
    for p in parts:
        print(p)
        if p == 'cooling':
            found_part = True
    assert type(parts) == list
    assert parts == "the"
    