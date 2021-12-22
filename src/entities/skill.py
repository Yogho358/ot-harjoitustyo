class Skill:
    def __init__(self, name, weapon, attack_modifier = 0, damage_modifier = 0, arena_size = "all"):
        self.name = name
        self.weapon = weapon
        self.attack_modifier = attack_modifier
        self.damage_modifier = damage_modifier
        self.arena_size = arena_size
        