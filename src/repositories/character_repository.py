import random
from entities.character import Character
from repositories.weapon_repository import weapon_repository
from database_connection import get_database_connection


def get_character_by_row(row):
    if row is None:
        return None
    weapon = weapon_repository.find_by_name(row["weapon"])
    return Character(row["name"],
                     row["current_hp"],
                     row["max_hp"],
                     weapon,
                     row["pc_or_npc"]) if row else None


class CharacterRepository:
    """Repository for saving all the characters
    """
    def __init__(self, connection):
        self.connection = connection

    def find_all(self):
        return self.find("pc")

    def find_enemies(self):
        return self.find("npc")

    def pick_enemy(self):
        """Chhoses a random enemy character from the database

        Returns:
            Character: The chosen npc
        """
        chars = self.find_enemies()
        return random.choice(chars)

    def find(self, pc_or_npc):
        """Finds either pcs or npcs from the database

        Args:
            pc_or_npc (string): whether looking for pcs or npcs

        Returns:
            list of Character: list of all characters in database matching pc or npc setting
        """
        cursor = self.connection.cursor()
        cursor.execute("select * from characters where pc_or_npc = ? order by name", (pc_or_npc,))
        rows = cursor.fetchall()
        return list(map(get_character_by_row, rows))

    def create(self, character):

        cursor = self.connection.cursor()

        cursor.execute(
            "insert into characters (name, current_hp, max_hp, weapon, pc_or_npc) values (?, ?, ?, ?, ?)",
            (character.name, character.current_hp, character.max_hp,
             character.weapon, character.pc_or_npc)
        )

        self.connection.commit()
        return self.find_by_character_name(character.name)

    def find_by_character_name(self, name):
        cursor = self.connection.cursor()
        cursor.execute("select * from characters where name = ?", (name,))

        row = cursor.fetchone()
        return get_character_by_row(row)

    def save_character(self, character):
        name = character.name
        current_hp = character.current_hp
        max_hp = character.max_hp
        weapon = character.weapon.name
        pc_or_npc = character.pc_or_npc
        sql = "update characters set current_hp = ?, max_hp = ?, weapon = ?, pc_or_npc = ? where name == ?"
        self.connection.execute(sql, (current_hp, max_hp, weapon, pc_or_npc, name))
        self.connection.commit()

    def clear(self):
        """deletes all Characters
        """
        cursor = self.connection.cursor()
        cursor.execute("delete from characters")
        self.connection.commit()


character_repository = CharacterRepository(get_database_connection())
