from app import app
import unittest
from repositories import builds_repo

def test_get_total_build_price():
    part = builds_repo.get_all_parts_for_table()
    if(len(part) <= 0):
        builds_repo.create_part('ARCTIC Liquid Freezer III 56.3 CFM Liquid CPU Cooler', 'cooling', 'cooling_image_4.jpg', 'https://example.com/cooling4', 'Brand D', 94.99, 4.2)
        part = builds_repo.get_all_parts_for_table()
    
    build_id = builds_repo.create_build(part, "gaming", "Great", False, 1, "")
    
    build_name = builds_repo.get_build_by_id(build_id)['build_name']
    total_price = 0
    for p in part:
        total_price += p['price']
    build_price = builds_repo.get_total_build_price(build_name)
    
    builds_repo.delete_build_by_id(build_id)
    assert total_price == build_price['sum']