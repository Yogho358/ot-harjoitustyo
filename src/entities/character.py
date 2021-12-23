
class Character:
    """Class for presenting player and non player characters.
        Attributes:
            name: character's name
            current_hp:
            max_hp:
            weapon: Weapon object the character is using
            pc_or_npc: Whether the character is meant to be played or to be an enemy
            skills: list of character's skills
            lvl_up_overwhelm: character got a level up due to overwhelming success
            lvl_up_desperation: character got a level up due to desperate situation
            different level ups are a placeholder, plan is to have different skills to be learnt from different circumstances 
    """
    def __init__(self, name, current_hp, max_hp, weapon, pc_or_npc, skills = [], lvl_up_overwhelm = False, lvl_up_desperation = False):
        self.name = name
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.weapon = weapon
        self.pc_or_npc = pc_or_npc
        self.skills = skills
        self.lvl_up_overwhelm = lvl_up_overwhelm
        self.lvl_up_desperation = lvl_up_desperation
