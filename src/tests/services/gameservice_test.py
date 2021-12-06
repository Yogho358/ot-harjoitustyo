import unittest
from services.gameservice import Gameservicepor
from initialize_database import initialize_database

class TestGameservice(unittest.TestCase):
    
    def setUp(self):
        initialize_database()
        self.gameservice = Gameservice()

    def test_create_and_find_character(self):
        self.gameservice.create_character("mr x", 20, 20, "longsword", "pc")
        char = self.gameservice.find_character("mr x")
        self.assertEqual(char.weapon.name, "longsword")

    def test_cannot_enter_arena_without_character(self):
        with self.assertRaises(Exception):
            self.gameservice.enter_arena()
