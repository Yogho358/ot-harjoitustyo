from entities.character import Character
from database_connection import get_database_connection


def get_character_by_row(row):
    return Character(row["name"],
                     row["current_hp"],
                     row["max_hp"],
                     row["weapon"],
                     row["pc_or_npc"]) if row else None


class CharacterRepository:
    def __init__(self, connection):
        self.connection = connection

    def find_all(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from characters where pc_or_npc = ?", ("pc",))
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

        return character

    def find_by_character_name(self, name):
        cursor = self.connection.cursor()
        cursor.execute("select * from characters where name = ?", (name,))

        row = cursor.fetchone()
        return get_character_by_row(row)

    def clear(self):
        self.characters = []


character_repository = CharacterRepository(get_database_connection())
