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

    def turn(self, player, command):
        """processes a single turn

        Args:
            player (string): whether it is player's or enemy's turn
            command (string): the action that is taken for the turn

        Returns:
            Boolean: whether the action succeeded
        """
        if command == "attack":
            if player == "pc":
                attacker = self.pc
                target = self.enemy
            else:
                attacker = self.enemy
                target = self.pc
            return self.attack(attacker, target)
        return

    def attack(self, attacker, target):
        attack_roll = random.randint(0, 100)
        if self.arena.size != attacker.weapon.size:
            attack_roll -= 10
        if attack_roll < target.weapon.chance_to_defend:
            return False

        damage = random.randint(attacker.weapon.min_dmg, attacker.weapon.max_dmg)
        target.current_hp -= damage
        return True
