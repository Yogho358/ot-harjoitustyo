import unittest
from repositories.character_repository import character_repository
from entities.character import Character

class TestCharacteRepository(unittest.TestCase):
    
    def setUp(self):
        character_repository.clear()

    def test_create(self):
        c = Character("mr x", 20, 20, "sword")
        character_repository.create(c)
        characters = character_repository.find_all()

        self.assertEqual(len(characters), 1)
        self.assertEqual(characters[0].name, "mr x")