import unittest
from services.battleservice import Battleservice
from entities.character import Character
from entities.weapon import Weapon
from entities.arena import Arena
from entities.skill import Skill

class TestBattleservice(unittest.TestCase):

    def setUp(self):

        weapon = Weapon("longsword", "large", 1, 1, 0)
        self.pc = Character("pc", 20, 20, weapon, "pc")
        self.npc = Character("npc", 20, 20, weapon, "npc")
        skill = Skill("half swording", "longsword", 0, 0, "all")
        self.pc.skills.append(skill)
        arena = Arena("large")
        self.battleservice = Battleservice(self.pc, self.npc, arena)

    def test_attack_works(self):
        self.assertEqual(self.battleservice.turn("pc", "attack"), True)

    def test_hp_decrease(self):
        self.battleservice.turn("npc", "attack")
        self.assertEqual(self.pc.current_hp, 19)

    def test_skill_attack_works(self):
        self.assertEqual(self.battleservice.turn("pc", "skill_attack", 1), True)

    def test_desperation_lvl_up_works(self):
        self.npc.current_hp = 0
        self.pc.current_hp = 1
        self.battleservice.battle_over()
        self.assertEqual(self.pc.lvl_up_desperation, True)

    def test_overwhelming_lvl_up_works(self):
        self.npc.current_hp = 0
        self.battleservice.battle_over()
        self.assertEqual(self.pc.lvl_up_overwhelm, True)