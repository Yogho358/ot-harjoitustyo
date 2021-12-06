import random


class Battleservice:
    def __init__(self, pc, enemy, arena):
        self.pc = pc
        self.enemy = enemy
        self.arena = arena

    def turn(self, player, command):
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
            attack_roll -= 20
        if attack_roll < target.weapon.chance_to_defend:
            return False

        damage = random.randint(attacker.weapon.min_dmg, attacker.weapon.max_dmg)
        target.current_hp -= damage
        return True
