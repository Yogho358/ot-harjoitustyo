
class Character:
    """Class for presenting player and non player characters.
        Attributes:
            name: character's name
            current_hp:
            max_hp:
            weapon: Weapon object the character is using
            pc_or_npc: Whether the character is meant to be played or to be an enemy
    """
    def __init__(self, name, current_hp, max_hp, weapon, pc_or_npc):
        self.name = name
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.weapon = weapon
        self.pc_or_npc = pc_or_npc
