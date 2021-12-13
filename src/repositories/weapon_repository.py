
from entities.weapon import Weapon
from database_connection import get_database_connection

def get_weapon_by_row(row):
    return Weapon(row["name"],
                  row["size"],
                  row["min_dmg"],
                  row["max_dmg"],
                  row["chance_to_defend"]) if row else None

class WeaponRepository:
    """Repository for Weapons in database
    """
    def __init__(self, connection):
        self._connection = connection

    def create(self, weapon):
        """Create a new weapon entry to the database

        Args:
            weapon (Weapon): Weapon object representing the new entry

        Returns:
            Weapon: returns the added weapon
        """
        cursor = self._connection.cursor()

        cursor.execute("insert into weapons (name, size, min_dmg, max_dmg, chance_to_defend) values (?, ?, ?, ?, ?)",
        (weapon.name, weapon.size, weapon.min_dmg, weapon.max_dmg, weapon.chance_to_defend)
        )

        self._connection.commit()

        return weapon

    def find_all(self):
        """finds all weapons

        Returns:
            list of Weapon: list of all weapons in the database
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from weapons order by name")
        rows = cursor.fetchall()
        return list(map(get_weapon_by_row, rows))

    def find_by_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute("select * from weapons where name = ?", (name,))
        row = cursor.fetchone()
        return get_weapon_by_row(row)

    def clear(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from weapons")
        self._connection.commit()

weapon_repository = WeaponRepository(get_database_connection())
