
from gui.battle_ui import BattleUi

COMMANDS = {
    "x": "x quit",
    "1": "1 New character",
    "2": "2 Load character",
    "3": "3 enter arena",
    "4": "4 list available weapons",
    "5": "5 list character's skills"
}


class Mainmenu:
    def __init__(self, io, gameservice):
        self.io = io
        self.gameservice = gameservice
        self.player_char = None
        

    def run(self):
        self.io.print("Welcome to the Game")
        self.print_commands()
        self.gameservice.pick_enemy()
        self.gameservice.next_arena()

        while True:
            self.player_char = self.gameservice.player_char
            if self.player_char != None:
                self.gameservice.save_player_character()
            if self.player_char == None:
                self.io.print("No character selected")
            elif self.player_char.current_hp <= 0:
                self.io.print(f"{self.player_char.name} is dead")
            else:
                self.io.print(f"{self.player_char.name} ready for adventure")
                self.io.print(f"You are about to face {self.gameservice.enemy.name} in a {self.gameservice.arena.size} arena")
            command = self.io.read("Command: ")
            if not command in COMMANDS:
                self.io.print("Invalid command")
                self.print_commands()
            if command == "x":
                break

            if command == "1":
                self.create_pc()

            if command == "2":
                self.select_pc()

            if command == "3":
                self.enter_arena()

            if command == "4":
                self.list_weapons()

            if command == "5":
                self.list_skills()

    def print_commands(self):
        for command in COMMANDS:
            self.io.print(COMMANDS[command])

    def create_pc(self):
        name = self.io.read("name: ")
        try:
            weapon = self.select_weapon()
        except Exception as e:
            self.io.print(e)
        try:
            self.gameservice.create_character(
                name=name, current_hp=20, max_hp=20, weapon=weapon, pc_or_npc="pc")
        except Exception as e:
            self.io.print(e)

    def select_pc(self):
        chars = self.gameservice.find_all()
        if len(chars) == 0:
            self.io.print("No characters available")
            return
     
        for i in range(len(chars)):
            rip = ""
            if chars[i].current_hp <= 0:
                rip = "RIP"
            self.io.print(f"{i+1}: {chars[i].name} {rip}")
        try:
            choice = int(self.io.read("number of choice: "))
        except ValueError:
            self.io.print("Must give a number")
            return
        try:
            char = chars[choice-1].name
        except Exception:
            self.io.print("No such character")
            return
        self.gameservice.set_player_char(char)

    def select_weapon(self):
        self.io.print("Choose a weapon")
        weapons = self.gameservice.find_all_weapons()
        if len(weapons) == 0:
            self.io.print("No weapons available")
            return

        weapon_indices =[]
        
        for i in range(len(weapons)):
            self.io.print(f"{i+1}: {weapons[i].name}")
            weapon_indices.append(i+1)
        try:
            choice = int(self.io.read("number of choice: "))
        except ValueError:
            self.io.print("Must give a number")
            return
        if choice not in weapon_indices:
            raise Exception("no such weapon")
        weapon_name = weapons[choice-1].name
        return weapon_name


    def enter_arena(self):
        try:
            battleservice = self.gameservice.enter_arena()
            arenamenu = BattleUi(battleservice)
            arenamenu.run()
        except Exception as e:
                    self.io.print(e)
            

    def list_weapons(self):
        weapons = self.gameservice.find_all_weapons()
        if len(weapons) == 0:
            self.io.print("No weapons available")
            return
        
        for weapon in weapons:
            self.io.print(f"{weapon.name}")

    def list_skills(self):
        
        for skill in self.player_char.skills:
            self.io.print(skill.name)

