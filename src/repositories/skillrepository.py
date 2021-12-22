from database_connection import get_database_connection
from entities.skill import Skill

def get_skill_by_row(row):
    return Skill(row["name"],
                row["weapon"],
                row["attack_modifier"],
                row["damage_modifier"],
                row["arena_size"]) if row else None

class SkillRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, skill):

        cursor = self._connection.cursor()
        cursor.execute(
            "insert into skills (name, weapon, attack_modifier, damage_modifier, arena_size) values (?, ?, ?, ?, ?)",
        (skill.name, skill.weapon, skill.attack_modifier, skill.damage_modifier, skill.arena_size))

        self._connection.commit()
        return skill

    def find_characters_skills(self, name, weapon):
        cursor = self._connection.cursor()
        cursor.execute(
            "select S.name, S.weapon, S.attack_modifier, S.damage_modifier, S.arena_size from skills S, characterskills C where C.character_name = ? and C.skill_name = S.name and S.weapon = ?",
        (name, weapon))
        rows = cursor.fetchall()
        return list(map(get_skill_by_row, rows))

    def clear(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from skills")
        self._connection.commit()

skill_repository = SkillRepository(get_database_connection())
