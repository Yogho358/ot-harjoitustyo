from entities.character import Character
from repositories.character_repository import character_repository
from repositories.arena_repository import arena_repository
from repositories.weapon_repository import weapon_repository
from repositories.skillrepository import skill_repository
from services.battleservice import Battleservice

class Gameservice:

    """Service that has the current state of the game
        Attributes:
            character repository: The repository where the characters can be found
            arena repository: for finding arenas
            weapon repository: for finding weapons
    """

    def __init__(self, character_repo = character_repository, arena_repo = arena_repository, weapon_repository = weapon_repository, skill_repository = skill_repository):
        self.player_char = None
        self.arena_repo = arena_repo
        self.enemy = None
        self.arena = None
        self.character_repo = character_repo
        self.weapon_repo = weapon_repository
        self.skill_repository = skill_repository

    def create_character(self, name, current_hp, max_hp, weapon, pc_or_npc):
        """Creates a new character and saves it to database, and adds it as a current player character

        Args:
            name (string): name of the new character, must be unique
            current_hp (int): current hps
            max_hp (int): max hps
            weapon (string): name of the weapon the character uses
            pc_or_npc (string): whether the character is meant to be played or to be an enemy
        """
        if len(name) == 0:
            raise Exception("Name cannot be empty")
        c = Character(name, current_hp, max_hp, weapon, pc_or_npc)
        self.set_player_char(self.character_repo.create(c).name)

    def pick_enemy(self):
        """picks a random enemy from database
        """
        self.enemy = self.character_repo.pick_enemy()

    def next_arena(self):
        self.arena = self.arena_repo.next_arena()

    def find_all(self):
        return self.character_repo.find_all()

    def find_character(self, name):
        return self.character_repo.find_by_character_name(name)

    def set_player_char(self, name):
        """finds a character from database and sets it as the current player character

        Args:
            name (string): name of the character
        """
        self.player_char = self.find_character(name)
        self.player_char.skills = self.find_players_skills()

    def enter_arena(self):
        """starts a battle in a new Battleservice

        Raises:
            Exception: Can't enter battle without a current character

        Returns:
            Battleservice: Service running the battle
        """
        if self.player_char is None or self.player_char.current_hp <= 0:
            raise Exception("You must select a living character")
        return Battleservice(self.player_char, self.enemy, self.arena)

    def find_all_weapons(self):
        return self.weapon_repo.find_all()

    def find_players_skills(self):
        """
        Finds the skills the current pc has that can be used with the current weapon
        """
        return self.skill_repository.find_characters_skills(self.player_char.name, self.player_char.weapon.name)

    def save_player_character(self):
        self.character_repo.save_character(self.player_char)

    def find_available_skills(self):
        """
        Finds the skills the current pc does not have but can be used with the current weapon
        """
        res = []
        skills = self.skill_repository.find_all()
        existing = []
        for skill in self.player_char.skills:
            existing.append(skill.name)

        for skill in skills:
            if skill.name not in existing and skill.weapon == self.player_char.weapon.name:
                res.append(skill)
        return res
    
    def add_skill_to_pc(self, skill):
        self.skill_repository.add_skill_to_character(self.player_char.name, skill.name)
        self.reset_lvl_up()
        self.set_player_char(self.player_char.name)

    def reset_lvl_up(self):
        self.player_char.lvl_up_overwhelm = False
        self.player_char.lvl_up_desperation = False

gameservice = Gameservice()
