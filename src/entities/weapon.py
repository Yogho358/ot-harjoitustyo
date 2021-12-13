
class Weapon:
    """Class for presenting weapons
    """
    def __init__(self, name, size, min_dmg, max_dmg, chance_to_defend):
        """Constructor that creates a new weapon

        Args:
            name (string): name of character
            size (string): size of weapon, small or large
            min_dmg (int): minimum possible damage
            max_dmg (int): maximum possible damage
            chance_to_defend (int): percentage chance to block enemy attack
        """
        self.name = name
        self.size = size
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.chance_to_defend = chance_to_defend
        