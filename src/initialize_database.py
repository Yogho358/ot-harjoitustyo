from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        drop table if exists characters;
    ''')
    cursor.execute('''
        drop table if exists weapons;
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
    
    cursor.execute('''
        create table weapons (
            name text primary key,
            size text,
            min_dmg integer,
            max_dmg integer,
            chance_to_defend
        );
        ''')

    connection.commit()

def add_enemy(connection):
    cursor = connection.cursor()
    cursor.execute("insert into characters (name, current_hp, max_hp, weapon, pc_or_npc) values (?, ?, ?, ?, ?)",
    ("swordsman", 20, 20, "longsword", "npc"))
    cursor.execute("insert into characters (name, current_hp, max_hp, weapon, pc_or_npc) values (?, ?, ?, ?, ?)",
    ("batmonster", 30, 30, "claw", "npc"))
    connection.commit()

def add_weapon(connection):
    cursor = connection.cursor()
    cursor.execute("insert into weapons (name, size, min_dmg, max_dmg, chance_to_defend) values (?, ?, ?, ?, ?)",
    ("longsword", "large", 2, 6, 65))
    cursor.execute("insert into weapons (name, size, min_dmg, max_dmg, chance_to_defend) values (?, ?, ?, ?, ?)",
    ("claw", "small", 1, 4, 25))
    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    add_enemy(connection)
    add_weapon(connection)

if __name__ == '__main__':
    initialize_database()
    