from entities.character import Character
from repositories.character_repository import character_repository

class Gameservice:

    def __init__(self,character_repo = character_repository):
        self.player_char = None
        self.character_repo = character_repo
        

    def create_character(self, name, current_hp, max_hp, weapon):
        c = Character(name,current_hp,max_hp,weapon)
        self.player_char = self.character_repo.create(c)

    def find_all(self):
        return self.character_repo.find_all()

    def find_character(self, name):
        return self.character_repo.find_by_character_name(name)

    def set_player_char(self, name):
        self.player_char = self.find_character(name)
        

gameservice = Gameservice()
