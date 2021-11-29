import unittest
from repositories.character_repository import character_repository
from entities.character import Character
from initialize_database import initialize_database

class TestCharacterRepository(unittest.TestCase):

    
    
    def setUp(self):
        initialize_database()
        c = Character("mr x", 30, 30, "sword", "pc")
        c2 = Character("mr a", 20, 20, "sword", "pc")
        character_repository.create(c)
        character_repository.create(c2)

    def test_find_all(self):
        
        characters = character_repository.find_all()
        self.assertEqual(len(characters),2)
        self.assertEqual(characters[0].name, "mr a")

    def test_find_by_character_name(self):
        
        character = character_repository.find_by_character_name("mr x")
        self.assertEqual(character.current_hp, 30)

    def test_find_by_wrong_character_name(self):
        character = character_repository.find_by_character_name("wrong")
        self.assertEqual(character, None)

