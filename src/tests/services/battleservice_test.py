import unittest
from services.battleservice import Battleservice
from entities.character import Character
from entities.weapon import Weapon
from entities.arena import Arena

class TestBattleservice(unittest.TestCase):

    def setUp(self):

        weapon = Weapon("longsword", "large", 1, 1, 0)
        self.pc = Character("pc", 20, 20, weapon, "pc")
        self.npc = Character("npc", 20, 20, weapon, "npc")
        arena = Arena("large")
        self.battleservice = Battleservice(self.pc, self.npc, arena)

    def test_attack_works(self):
        self.assertEqual(self.battleservice.turn("pc", "attack"), True)

    def test_hp_decrease(self):
        self.battleservice.turn("npc", "attack")
        self.assertEqual(self.pc.current_hp, 19)