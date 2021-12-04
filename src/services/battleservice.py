from repositories.weapon_repository import weapon_repository

class Battleservice:
    def __init__(self, pc, enemy, arena, weapon_repo = weapon_repository):
        self.pc = pc
        self.enemy = enemy
        self.arena = arena
        self._weapon_repo = weapon_repo
        self.pc_weapon = self._weapon_repo.find_by_name(self.pc.weapon)