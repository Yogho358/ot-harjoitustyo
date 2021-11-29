from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        drop table if exists characters;
    ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table characters (
            name text primary key,
            current_hp integer,
            max_hp integer,
            weapon text,
            pc_or_npc text
        );
        ''')

    connection.commit()

def add_enemy(connection, name, current_hp, max_hp, weapon, pc_or_npc):
    cursor = connection.cursor()
    cursor.execute("insert into characters (name, current_hp, max_hp, weapon, pc_or_npc) values (?, ?, ?, ?, ?)",
    ("swordsman", 20, 20, "longsword", "npc"))
    cursor.execute("insert into characters (name, current_hp, max_hp, weapon, pc_or_npc) values (?, ?, ?, ?, ?)",
    ("batmonster", 30, 30, "claws", "npc"))
    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    add_enemy(connection, "swordman", 20, 20, "longsword", "npc")

if __name__ == '__main__':
    initialize_database()