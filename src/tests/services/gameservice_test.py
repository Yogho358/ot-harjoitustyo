import unittest
from services.gameservice import Gameservice
from initialize_database import initialize_database
from entities.skill import Skill

class TestGameservice(unittest.TestCase):
    
    def setUp(self):
        initialize_database()
        self.gameservice = Gameservice()
        self.gameservice.create_character("mr x", 20, 20, "longsword", "pc")

    def test_create_and_find_character(self):      
        char = self.gameservice.find_character("mr x")
        self.assertEqual(char.weapon.name, "longsword")

    def test_cannot_enter_arena_without_character(self):
        self.gameservice.player_char = None
        with self.assertRaises(Exception):
            self.gameservice.enter_arena()

    def test_add_skill_to_pc(self):
        skill = Skill("half swording", "longsword", 2, 0, "small")
        self.gameservice.add_skill_to_pc(skill)
        self.assertEqual(self.gameservice.player_char.skills[0].name, "half swording")

    def test_find_available_skills(self):
        skill = Skill("half swording", "longsword", 2, 0, "small")
        self.gameservice.add_skill_to_pc(skill)
        skills = self.gameservice.find_available_skills()
        self.assertEqual(skills[0].name, "overhead swing")

    def test_skill_not_available_if_weapon_different(self):
        self.gameservice.create_character("mr y", 20, 20, "short swords", "pc")
        skill = Skill("half swording", "longsword", 2, 0, "small")
        self.gameservice.add_skill_to_pc(skill)
        skills = self.gameservice.find_available_skills()
        self.assertNotIn("overhead swing", skills)
