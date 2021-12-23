from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        drop table if exists characters;
    ''')
    cursor.execute('''
        drop table if exists weapons;
        ''')

    cursor.execute('''
        drop table if exists skills;
        ''')

    cursor.execute('''
        drop table if exists characterskills;
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

    cursor.execute('''
        create table skills (
            name text primary key,
            weapon text,
            attack_modifier integer,
            damage_modifier integer,
            arena_size text
        );
        ''')

    cursor.execute('''
        create table characterskills (
            character_name text,
            skill_name text
        );
        ''')

    connection.commit()

def add_enemy(connection):
    cursor = connection.cursor()
    cursor.execute(
        "insert into characters (name, current_hp, max_hp, weapon, pc_or_npc) values (?, ?, ?, ?, ?)",
    ("swordsman", 20, 20, "longsword", "npc"))
    cursor.execute(
        "insert into characters (name, current_hp, max_hp, weapon, pc_or_npc) values (?, ?, ?, ?, ?)",
    ("batmonster", 30, 30, "claw", "npc"))
    connection.commit()

def add_weapon(connection):
    cursor = connection.cursor()
    cursor.execute("insert into weapons (name, size, min_dmg, max_dmg, chance_to_defend) values (?, ?, ?, ?, ?)",
    ("longsword", "large", 2, 6, 65))
    cursor.execute("insert into weapons (name, size, min_dmg, max_dmg, chance_to_defend) values (?, ?, ?, ?, ?)",
    ("claw", "small", 1, 4, 25))
    cursor.execute("insert into weapons (name, size, min_dmg, max_dmg, chance_to_defend) values (?, ?, ?, ?, ?)",
    ("short swords", "small", 1, 5, 45))
    connection.commit()

def add_skill(connection):
    cursor = connection.cursor()
    cursor.execute(
        "insert into skills (name, weapon, attack_modifier, damage_modifier, arena_size) values (?, ?, ?, ?, ?)",
    ("double stab", "short swords", 0, 2, "all"))
    cursor.execute(
        "insert into skills (name, weapon, attack_modifier, damage_modifier, arena_size) values (?, ?, ?, ?, ?)",
    ("off-hand distraction", "short swords", 2, -2, "all"))
    cursor.execute(
        "insert into skills (name, weapon, attack_modifier, damage_modifier, arena_size) values (?, ?, ?, ?, ?)",
    ("half swording", "longsword", 2, 0, "small"))
    cursor.execute(
        "insert into skills (name, weapon, attack_modifier, damage_modifier, arena_size) values (?, ?, ?, ?, ?)",
    ("overhead swing", "longsword", -2, 4, "large"))
    cursor.execute("insert into characterskills (character_name, skill_name) values (?, ?)",
    ("Mr X", "double stab"))
    cursor.execute("insert into characterskills (character_name, skill_name) values (?, ?)",
    ("Mr X", "half swording"))
    connection.commit()

def add_character(connection):
    cursor = connection.cursor()
    cursor.execute("insert into characters (name, current_hp, max_hp, weapon, pc_or_npc) values (?, ?, ?, ?, ?)",
    ("Mr X", 20, 20, "longsword", "pc"))
    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    add_enemy(connection)
    add_weapon(connection)
    add_skill(connection)
    add_character(connection)

if __name__ == '__main__':
    initialize_database()
    