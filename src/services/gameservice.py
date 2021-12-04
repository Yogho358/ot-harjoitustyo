from entities.character import Character
from repositories.character_repository import character_repository
from repositories.arena_repository import arena_repository
from services.battleservice import Battleservice

class Gameservice:

    def __init__(self, character_repo = character_repository, arena_repo = arena_repository):
        self.player_char = None
        self.enemy = character_repo.pick_enemy()
        self.arena = arena_repo.next_arena()
        self.character_repo = character_repo

    def create_character(self, name, current_hp, max_hp, weapon, pc_or_npc):
        c = Character(name, current_hp, max_hp, weapon, pc_or_npc)
        self.player_char = self.character_repo.create(c)

    def find_all(self):
        return self.character_repo.find_all()

    def find_character(self, name):
        return self.character_repo.find_by_character_name(name)

    def set_player_char(self, name):
        self.player_char = self.find_character(name)

    def get_enemy(self):
        return self.enemy

    def get_arena(self):
        return self.arena

    def enter_arena(self):
        return Battleservice(self.player_char, self.enemy, self.arena)

gameservice = Gameservice()
