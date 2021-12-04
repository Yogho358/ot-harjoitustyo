import unittest
from repositories.weapon_repository import weapon_repository
from entities.weapon import Weapon
from initialize_database import initialize_database

class TestWeaponRepository(unittest.TestCase):

    def setUp(self):
        initialize_database()
        weapon_repository.clear()
        w1 = Weapon("longswordtest", "large", 2, 6, 50)
        w2 = Weapon("shortswordtest", "small", 1, 4, 40)
        weapon_repository.create(w1)
        weapon_repository.create(w2)
    
    def test_find_all(self):
        weapons = weapon_repository.find_all()
        self.assertEqual(len(weapons), 2)
        self.assertEqual(weapons[1].size, "small")
    