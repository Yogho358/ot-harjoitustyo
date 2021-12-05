from entities.character import Character
from repositories.character_repository import character_repository
from repositories.arena_repository import arena_repository
from repositories.weapon_repository import weapon_repository
from services.battleservice import Battleservice

class Gameservice:

    def __init__(self, character_repo = character_repository, arena_repo = arena_repository, weapon_repository = weapon_repository):
        self.player_char = None
        self.arena_repo = arena_repo
        self.enemy = None
        self.arena = None
        self.character_repo = character_repo
        self.weapon_repo = weapon_repository

    def create_character(self, name, current_hp, max_hp, weapon, pc_or_npc):
        c = Character(name, current_hp, max_hp, weapon, pc_or_npc)
        self.player_char = self.character_repo.create(c)

    def pick_enemy(self):
        self.enemy = self.character_repo.pick_enemy()

    def next_arena(self):
        self.arena = self.arena_repo.next_arena()

    def find_all(self):
        return self.character_repo.find_all()

    def find_character(self, name):
        return self.character_repo.find_by_character_name(name)

    def set_player_char(self, name):
        self.player_char = self.find_character(name)

    def enter_arena(self):
        if self.player_char is None:
            raise Exception("You must select a character")
        return Battleservice(self.player_char, self.enemy, self.arena)

    def find_all_weapons(self):
        return self.weapon_repo.find_all()

gameservice = Gameservice()
