import random


class Battleservice:
    """Processes what happens during battle turns
        Attributes:
            pc: player character
            enemy: enemy character
            arena: Battle arena
    """
    def __init__(self, pc, enemy, arena):
        """Construktor creating a new battle

        Args:
            pc (Character): player character
            enemy (Character): enemy character
            arena (Arena): battle arena
        """
        self.pc = pc
        self.enemy = enemy
        self.arena = arena
        self._attack_modifier = 0
        self._damage_modifier = 0

    def turn(self, player, command, option = None):
        """processes a single turn

        Args:
            player (string): whether it is player's or enemy's turn
            command (string): the action that is taken for the turn

        Returns:
            Boolean: whether the action succeeded
        """
        if player == "pc":
            actor = self.pc
            target = self.enemy
        else:
            actor = self.enemy
            target = self.pc

        if command == "attack":
            return self.attack(actor, target)
        if command == "skill_attack":
            return self.attack_with_skill(actor, target, option)
        return

    def attack(self, attacker, target):
        attack_roll = random.randint(0, 100) + self._attack_modifier
        if self.arena.size == "small" and attacker.weapon.size == "large":
            attack_roll -= 10

        if attack_roll < target.weapon.chance_to_defend:
            return False

        damage = random.randint(attacker.weapon.min_dmg, attacker.weapon.max_dmg)
        target.current_hp -= damage + self._damage_modifier
        return True

    def attack_with_skill(self, attacker, target, skill_number):
        skill = self.pc.skills[skill_number-1]
        if skill.arena_size == self.arena.size or skill.arena_size == "all":
            self._attack_modifier += skill.attack_modifier
            self._damage_modifier += skill.damage_modifier

        hit = self.attack(attacker, target)
        self.reset_modifiers()
        return hit

    def reset_modifiers(self):
        self._attack_modifier = 0
        self._damage_modifier = 0

    def battle_over(self):
        return self.pc.current_hp <= 0 or self.enemy.current_hp <= 0
