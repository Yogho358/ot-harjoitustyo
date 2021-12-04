import unittest
from services.gameservice import Gameservice
#from entities.character import Character
from initialize_database import initialize_database

# class FakeCharacterRepository:
#     def __init__(self, characters = []):
#         self.characters = characters

#     def find_all(self):
#         return self.characters

#     def create(self, character):  
#         self.characters.append(Character(character.name, character.current_hp, character.max_hp, character.weapon, character.pc_or_npc))
        
#     def find_by_character_name(self, name):
#         character = None
#         for c in self.characters:
#             if c.name == name:
#                 character = c

#         return character

#     def pick_enemy(self):
#         return Character("swordsman", 20, 20, "longsword", "npc")

class TestGameservice(unittest.TestCase):
    
    def setUp(self):
        initialize_database()
        self.gameservice = Gameservice()

    def test_create_and_find_character(self):
        self.gameservice.create_character("mr x", 20, 20, "sword", "pc")
        char = self.gameservice.find_character("mr x")
        self.assertEqual(char.weapon, "sword")

    def test_cannot_enter_arena_without_character(self):
        with self.assertRaises(Exception):
            self.gameservice.enter_arena()
